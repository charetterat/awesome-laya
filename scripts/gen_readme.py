#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render README.md from data/laya.json.

Single source of truth: data/laya.json.
Running with --check exits non-zero if the rendered file has drifted,
serving as our mandatory CI gate.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "README.md")


def load(name):
    with open(os.path.join(ROOT, "data", name), encoding="utf-8") as f:
        return json.load(f)


def table(headers, rows, align=None):
    align = align or ["---"] * len(headers)
    out = ["| " + " | ".join(headers) + " |",
           "|" + "|".join(align) + "|"]
    for r in rows:
        out.append("| " + " | ".join(str(c) for c in r) + " |")
    return "\n".join(out)


def main():
    d = load("laya.json")
    layers = d["layers"]
    items = [i for l in layers for i in l["items"]]
    n_items = len(items)
    langs = sorted({i["language"] for i in items if i.get("language")})

    # Data-driven ecosystem tree (no hand-aligned ASCII: emoji are double-width).
    branches = layers[1:]
    tlines = ["```",
              f"Laya (core engine)  ·  typed decisions in one forward pass · {len(langs)} languages",
              "│"]
    for idx, layer in enumerate(branches):
        branch = "└──" if idx == len(branches) - 1 else "├──"
        names = " · ".join(x["name"] for x in layer["items"])
        tlines.append(f"{branch} {layer['icon']} {layer['layer_name']}  →  {names}")
    tlines.append("```")
    eco_tree = "\n".join(tlines)

    L = []
    L.append(f"""<div align="center">

# awesome-laya

**The ecosystem index for [Laya](https://github.com/NandhaKishorM/laya) — the open, non-autoregressive System 1 decision engine.**

Runtimes, language ports, servers, MCP connectors, and apps. {n_items} repositories across {len(langs)} languages — every entry a real, independently-usable repo, verified live.

[![Sources Verified](https://img.shields.io/badge/CI-Sources%20Verified-brightgreen)](scripts/verify_sources.py)
[![Repos](https://img.shields.io/badge/repos-{n_items}-blue)](https://github.com/NandhaKishorM/laya)
[![Languages](https://img.shields.io/badge/languages-{len(langs)}-violet)](#-language-runtimes--ports)
[![License](https://img.shields.io/badge/license-CC--BY--4.0-lightgrey.svg)](LICENSE)

> ⛔ **Not affiliated with Laya, ConvAI Innovations, or any project listed.** Star counts are a live snapshot ({d['updated']}).

</div>

---

## 🤔 What is Laya?

{ d['model']['what'] }

Instead of paying an LLM to call a tool, read a page, or sort a request, you run one local forward pass and get a typed answer in milliseconds. That single idea has spawned a fast-growing ecosystem — runtimes, servers, SDKs, and integrations — which is what this list tracks.

---

## ⚡ Pick your entry point

| I want to… | Go to |
|---|---|
| Run Laya as fast as possible (Apple Silicon) | [laya-mlx](https://github.com/mizorewww/laya-mlx) |
| Call Laya from Node.js / TypeScript | [receptron/laya](https://github.com/receptron/laya) |
| Call Laya from C++ (CUDA / Vulkan) | [laya.cpp](https://github.com/lkarlslund/laya.cpp) |
| Call Laya from Go | [laya-go](https://github.com/neko233-com/laya-go) |
| Call Laya from Java | [Laya4j](https://github.com/githubMJ/Laya4j) |
| Call Laya from PHP / Laravel | [laya-php](https://github.com/marcreichel/laya-php) |
| Serve Laya behind a local API | [ollaya](https://github.com/ollaya-dev/ollaya) |
| Self-host with a web UI | [laya-server](https://github.com/1Panel-dev/laya-server) |
| Give my agent Laya over MCP | [system-one-connector](https://github.com/itsmostafa/system-one-connector) |
| Route requests to the right model | [laya_router](https://github.com/glukicov/laya_router) |
| Turn vague requests into typed intents | [Intent-Router](https://github.com/angel291592/Intent-Router) |
| Evaluate agent traces cheaply | [jevals](https://github.com/openlayer-ai/jevals) |
| Add image inputs | [laya-vision](https://github.com/r33drichards/laya-vision) |
| Decide Laya vs Jev | [laya-vs-jev](https://github.com/virajbhartiya/laya-vs-jev) |
| See it running, no setup | [laya-playground](https://github.com/wdobry/laya-playground) |

---

## 🗺️ Map of the ecosystem

{eco_tree}

---

## 📚 Full index

""")

    for i, layer in enumerate(layers, 1):
        L.append(f"### {layer['icon']} {i}. {layer['layer_name']}\n\n{layer['description']}\n\n")
        L.append(table(
            ["Project", "Role", "Lang", "★"],
            [[f"[{x['name']}]({x['url']})", x["role"], x.get("language") or "-", f"{x['stars']:,}"]
             for x in layer["items"]],
            ["---", "---", "---", "---:"]
        ))
        L.append("\n\n")

    L.append("""---

## 🔍 Detailed breakdown

""")

    for layer in layers:
        L.append(f"### {layer['icon']} {layer['layer_name']}\n\n")
        for x in layer["items"]:
            lic = f" · `{x['license']}`" if x.get("license") and x["license"] != "None" else ""
            L.append(f"""#### [{x['name']}]({x['url']}) · ★{x['stars']:,}

> **{x['role']}**{lic}

{x['what']}

- **Key capabilities:** {x['key_capabilities']}

""")
        L.append("---\n\n")

    L.append(f"""## ✅ Source verification

Every repository in this list is checked for reachability by CI:

```bash
python3 scripts/verify_sources.py
```

The gate fails loudly if a cited source goes dark, so the index cannot silently rot.

---

<div align="center">

**Data** — [`data/laya.json`](data/laya.json) · **Validator** — [`scripts/verify_sources.py`](scripts/verify_sources.py)

<sub>README.md is generated from data/laya.json. Edit the JSON, not this file.</sub>

</div>
""")

    text = "\n".join(L)

    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
        if cur != text:
            sys.exit("README.md is stale — run: python3 scripts/gen_readme.py")
        print("README.md in sync")
        return

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {OUT} ({len(text):,} chars)")


if __name__ == "__main__":
    main()
