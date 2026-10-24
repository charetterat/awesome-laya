<div align="center">

# awesome-laya

**The ecosystem index for [Laya](https://github.com/NandhaKishorM/laya) — the open, non-autoregressive System 1 decision engine.**

Runtimes, language ports, servers, MCP connectors, and apps. 29 repositories across 11 languages — every entry a real, independently-usable repo, verified live.

[![Sources Verified](https://img.shields.io/badge/CI-Sources%20Verified-brightgreen)](scripts/verify_sources.py)
[![Repos](https://img.shields.io/badge/repos-29-blue)](https://github.com/NandhaKishorM/laya)
[![Languages](https://img.shields.io/badge/languages-11-violet)](#-language-runtimes--ports)
[![License](https://img.shields.io/badge/license-CC--BY--4.0-lightgrey.svg)](LICENSE)

> ⛔ **Not affiliated with Laya, ConvAI Innovations, or any project listed.** Star counts are a live snapshot (2026-10-25).

</div>

---

## 🤔 What is Laya?

A non-autoregressive System 1 decision engine. Instead of generating text, it returns a typed decision — choice, score, or yes/no — over any input in a single forward pass, in 100+ languages.

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

```
Laya (core engine)  ·  typed decisions in one forward pass · 11 languages
│
├── ⚙️ Language Runtimes & Ports  →  laya-mlx · laya-coreml · laya.cpp · laya · laya-php · lev · Laya4j · laya-go · laya-Ascend · laya-vision
├── 🚀 Serving & Self-Hosting  →  ollaya · laya-server · arbiter
├── 🤖 Agent Integration  →  system-one-connector · FluidUse · system1-agents · omp-laya-judge · home-assistant-laya
├── 🎮 Applications & Demos  →  keel · laya-ultrafast · WechatVibe · laya-playground · laya-vs-jev
└── 🔀 Routing, Eval & Related Models  →  Intent-Router · laya_router · jevals · openJev-verdict-2.0 · OpenJev
```

---

## 📚 Full index


### 🧠 1. Core Engine

The model itself. Non-autoregressive System 1 decision engine — typed choice / score / yes-no over any text in a single forward pass, 100+ languages.


| Project | Role | Lang | ★ |
|---|---|---|---:|
| [laya](https://github.com/NandhaKishorM/laya) | Core | Python | 32,160 |



### ⚙️ 2. Language Runtimes & Ports

Run Laya on your stack — no Python service required. Ports and native runtimes across 10 languages and accelerators.


| Project | Role | Lang | ★ |
|---|---|---|---:|
| [laya-mlx](https://github.com/mizorewww/laya-mlx) | Runtime · Apple MLX | Python | 6,864 |
| [laya-coreml](https://github.com/mizorewww/laya-coreml) | Runtime · Apple Core ML | Python | 1,571 |
| [laya.cpp](https://github.com/lkarlslund/laya.cpp) | Runtime · C++ | C++ | 123 |
| [laya](https://github.com/receptron/laya) | Runtime · TypeScript / Node.js | TypeScript | 880 |
| [laya-php](https://github.com/marcreichel/laya-php) | SDK · PHP | PHP | 88 |
| [lev](https://github.com/jlt-commons/lev) | Port · Clojure | Clojure | 28 |
| [Laya4j](https://github.com/githubMJ/Laya4j) | SDK · Java | Java | 7 |
| [laya-go](https://github.com/neko233-com/laya-go) | Port · Go | Go | 5 |
| [laya-Ascend](https://github.com/zzhdbw/laya-Ascend) | Port · Ascend NPU | Python | 110 |
| [laya-vision](https://github.com/r33drichards/laya-vision) | Extension · Multimodal | Python | 83 |



### 🚀 3. Serving & Self-Hosting

Stand up a local decision API — the 'Ollama for decision models' layer. Pull, serve, and call typed decisions behind a familiar HTTP interface.


| Project | Role | Lang | ★ |
|---|---|---|---:|
| [ollaya](https://github.com/ollaya-dev/ollaya) | Server · Ollama-style | Rust | 1,282 |
| [laya-server](https://github.com/1Panel-dev/laya-server) | Server · Self-hosted + Web UI | Python | 98 |
| [arbiter](https://github.com/0xBakeer/arbiter) | Server · GPU | HTML | 34 |



### 🤖 4. Agent Integration

Wire Laya into an agent as a fast, cheap judgment layer — MCP servers, frameworks, and platform bindings.


| Project | Role | Lang | ★ |
|---|---|---|---:|
| [system-one-connector](https://github.com/itsmostafa/system-one-connector) | MCP Server | Go | 349 |
| [FluidUse](https://github.com/FluidInference/FluidUse) | Framework · Computer Use | Swift | 305 |
| [system1-agents](https://github.com/ThinkFlowLab/system1-agents) | Framework · Multi-domain | Python | 131 |
| [omp-laya-judge](https://github.com/F0Rextasy/omp-laya-judge) | MCP Server + Skill | HTML | 7 |
| [home-assistant-laya](https://github.com/allenporter/home-assistant-laya) | Binding · Home Assistant | Python | 9 |



### 🎮 5. Applications & Demos

Real products and runnable demos that show Laya replacing an LLM call for a specific job.


| Project | Role | Lang | ★ |
|---|---|---|---:|
| [keel](https://github.com/codejunkie99/keel) | App · macOS Coding Workspace | Rust | 330 |
| [laya-ultrafast](https://github.com/ipenywis/laya-ultrafast) | App · Web Agent | Python | 252 |
| [WechatVibe](https://github.com/tswawa/WechatVibe) | App · Chat Analysis | Python | 248 |
| [laya-playground](https://github.com/wdobry/laya-playground) | Playground · Benchmark + Skill | JavaScript | 185 |
| [laya-vs-jev](https://github.com/virajbhartiya/laya-vs-jev) | Demo · Head-to-head | Python | 111 |



### 🔀 6. Routing, Eval & Related Models

The judgment layer around the model — intent contracts, routers, evals, and the sibling decision engines that share Laya's API.


| Project | Role | Lang | ★ |
|---|---|---|---:|
| [Intent-Router](https://github.com/angel291592/Intent-Router) | Router · Input Layer | Python | 1,068 |
| [laya_router](https://github.com/glukicov/laya_router) | Router · Model Selection | Python | 13 |
| [jevals](https://github.com/openlayer-ai/jevals) | Eval · Guardrails | Python | 103 |
| [openJev-verdict-2.0](https://github.com/Heman10x-NGU/openJev-verdict-2.0) | Sibling Model · Verdict | Python | 295 |
| [OpenJev](https://github.com/zhangcy122/OpenJev) | Sibling Model · Open | Python | 40 |



---

## 🔍 Detailed breakdown


### 🧠 Core Engine


#### [laya](https://github.com/NandhaKishorM/laya) · ★32,160

> **Core** · `Apache-2.0`

The reference implementation. One forward pass returns a typed decision (choice, score, or yes/no) instead of generated text, plus a router that picks the right checkpoint per request.

- **Key capabilities:** 100+ languages · router-selected checkpoints · calibration-aware · Apache-2.0


---


### ⚙️ Language Runtimes & Ports


#### [laya-mlx](https://github.com/mizorewww/laya-mlx) · ★6,864

> **Runtime · Apple MLX** · `Apache-2.0`

Native MLX runtime. 7–14 ms short decisions on an M3 Max, with no text generation, no PyTorch, and no cloud API.

- **Key capabilities:** Apple MLX · 7–14 ms · fully local


#### [laya-coreml](https://github.com/mizorewww/laya-coreml) · ★1,571

> **Runtime · Apple Core ML** · `Apache-2.0`

Runs typed decisions on Core ML and the Neural Engine. ~5 ms short decisions on M3 Max, with reproducible speed and energy benchmarks.

- **Key capabilities:** Core ML · Neural Engine · ~5 ms


#### [laya.cpp](https://github.com/lkarlslund/laya.cpp) · ★123

> **Runtime · C++** · `MIT`

C++ inference for Laya typed decisions, with CUDA, Vulkan, Core ML, and CPU backends.

- **Key capabilities:** CUDA · Vulkan · Core ML · CPU


#### [laya](https://github.com/receptron/laya) · ★880

> **Runtime · TypeScript / Node.js** · `MIT`

Run the open-source Jev-compatible Laya model from Node.js and TypeScript via ONNX Runtime.

- **Key capabilities:** ONNX Runtime · Node.js · TypeScript


#### [laya-php](https://github.com/marcreichel/laya-php) · ★88

> **SDK · PHP** · `Apache-2.0`

Classify text in PHP without an LLM bill — typed decisions in 100+ languages, self-hosted. Laravel-ready.

- **Key capabilities:** Laravel-ready · self-hosted


#### [lev](https://github.com/jlt-commons/lev) · ★28

> **Port · Clojure** · `Apache-2.0`

A Jolt (Clojure on the JVM) implementation of the Laya non-autoregressive decision engine.

- **Key capabilities:** Jolt · JVM


#### [Laya4j](https://github.com/githubMJ/Laya4j) · ★7

> **SDK · Java**

Pure Java 17+ SDK that ports the Laya framework into a production-grade inference library, running fully on the Apache-2.0 checkpoints via ONNX Runtime and HuggingFace Hub.

- **Key capabilities:** Java 17+ · ONNX Runtime · HF Hub


#### [laya-go](https://github.com/neko233-com/laya-go) · ★5

> **Port · Go** · `MIT`

Go server plus agent CLI/MCP replacing JEV with open horizontal System 1 decision models (non-autoregressive structured prediction).

- **Key capabilities:** Go server · MCP · CLI


#### [laya-Ascend](https://github.com/zzhdbw/laya-Ascend) · ★110

> **Port · Ascend NPU** · `Apache-2.0`

Runs Laya checkpoints on Huawei Ascend NPUs.

- **Key capabilities:** Ascend NPU


#### [laya-vision](https://github.com/r33drichards/laya-vision) · ★83

> **Extension · Multimodal** · `Apache-2.0`

Image inputs for Laya — calibrated, non-generative typed decisions over images + text (SmolVLM-256M backbone).

- **Key capabilities:** Image+text · SmolVLM backbone


---


### 🚀 Serving & Self-Hosting


#### [ollaya](https://github.com/ollaya-dev/ollaya) · ★1,282

> **Server · Ollama-style** · `Apache-2.0`

Run open decision models locally: pull and serve Laya, decider, NLI, and GLiClass behind a TypeSafe-compatible API. 'Ollama for decision models.'

- **Key capabilities:** pull & serve · TypeSafe-compatible API


#### [laya-server](https://github.com/1Panel-dev/laya-server) · ★98

> **Server · Self-hosted + Web UI** · `Apache-2.0`

A self-hosted API and web interface for Laya's structured decision models, compatible with the TypeSafe Jev API format.

- **Key capabilities:** Web UI · Jev API format


#### [arbiter](https://github.com/0xBakeer/arbiter) · ★34

> **Server · GPU** · `MIT`

Serve typed-decision (System 1) models — Laya or your own — on NVIDIA GPUs or Apple Silicon, with a Jev-compatible API and coding-agent integrations.

- **Key capabilities:** NVIDIA GPU · Apple Silicon


---


### 🤖 Agent Integration


#### [system-one-connector](https://github.com/itsmostafa/system-one-connector) · ★349

> **MCP Server** · `MIT`

System One MCP connector to evaluate anything fast and cheap — gives your AI agent direct access to Jev, D1, CLM, and Laya.

- **Key capabilities:** MCP · agent-native


#### [FluidUse](https://github.com/FluidInference/FluidUse) · ★305

> **Framework · Computer Use** · `Apache-2.0`

Local computer use on Apple silicon: on-device typed decisions with Laya and form filling with CUA-S1-FORMS, driven through the macOS Accessibility API.

- **Key capabilities:** macOS Accessibility API · Apple silicon


#### [system1-agents](https://github.com/ThinkFlowLab/system1-agents) · ★131

> **Framework · Multi-domain** · `Apache-2.0`

System 1 decision models (Jev, Laya, Cua-S1) as the brain for agents: browser use, computer use, games, and robotics.

- **Key capabilities:** browser/computer use · robotics


#### [omp-laya-judge](https://github.com/F0Rextasy/omp-laya-judge) · ★7

> **MCP Server + Skill** · `NOASSERTION`

Local Laya System-1 judge MCP server and skill for oh-my-pi: typed decisions in milliseconds, zero LLM tokens.

- **Key capabilities:** oh-my-pi · zero tokens


#### [home-assistant-laya](https://github.com/allenporter/home-assistant-laya) · ★9

> **Binding · Home Assistant** · `Apache-2.0`

A Home Assistant conversation agent backed by Laya, the multilingual non-autoregressive System 1 decision model.

- **Key capabilities:** Home Assistant · conversation agent


---


### 🎮 Applications & Demos


#### [keel](https://github.com/codejunkie99/keel) · ★330

> **App · macOS Coding Workspace** · `MIT`

A local-first macOS coding workspace that uses local Laya and optional Jev decision selection.

- **Key capabilities:** local-first · macOS


#### [laya-ultrafast](https://github.com/ipenywis/laya-ultrafast) · ★252

> **App · Web Agent** · `MIT`

The ultrafast web-agent loop, rebuilt on Laya instead of a hosted model.

- **Key capabilities:** web agent · ultrafast


#### [WechatVibe](https://github.com/tswawa/WechatVibe) · ★248

> **App · Chat Analysis** · `Apache-2.0`

微信聊天分析工具：本地 Laya ＋ API 模型，提供意图识别、情绪感知、人物画像、群聊画像、好感度与 MBTI 推测。

- **Key capabilities:** 意图识别 · 情绪感知 · 人物画像


#### [laya-playground](https://github.com/wdobry/laya-playground) · ★185

> **Playground · Benchmark + Skill** · `MIT`

A website, two games, a benchmark, and an agent skill for Laya — all running on your machine.

- **Key capabilities:** live playground · benchmark · skill


#### [laya-vs-jev](https://github.com/virajbhartiya/laya-vs-jev) · ★111

> **Demo · Head-to-head** · `Apache-2.0`

Laya vs Jev: local MLX and hosted AI decisions playing T-Rex side by side, with live metrics and replay recording.

- **Key capabilities:** side-by-side · live metrics


---


### 🔀 Routing, Eval & Related Models


#### [Intent-Router](https://github.com/angel291592/Intent-Router) · ★1,068

> **Router · Input Layer** · `MIT`

Intent compiler for AI agents — converges vague requests into typed IntentSpec contracts (probe, ask, or halt before routing). The input layer for routers and typed-decision models like Jev and Laya.

- **Key capabilities:** IntentSpec contracts · probe/ask/halt


#### [laya_router](https://github.com/glukicov/laya_router) · ★13

> **Router · Model Selection** · `Apache-2.0`

Model routing as a System 1 job: a 421M local decision engine (Laya) vs a GPT-5-nano reasoning router — same accuracy, 35x faster, free.

- **Key capabilities:** 421M router · 35x faster


#### [jevals](https://github.com/openlayer-ai/jevals) · ★103

> **Eval · Guardrails** · `MIT`

Agent evals and guardrails as Jev-shaped decisions: one request per trace, a fraction of a cent, fast enough for the agent loop. Runs locally with Kev or Laya.

- **Key capabilities:** agent evals · guardrails


#### [openJev-verdict-2.0](https://github.com/Heman10x-NGU/openJev-verdict-2.0) · ★295

> **Sibling Model · Verdict** · `NOASSERTION`

A calibrated 151M non-autoregressive decision engine benchmarked against TypeSafe Jev and Laya (77.10% acc, 0.0636 Brier, 0.0144 ECE).

- **Key capabilities:** 151M · calibrated


#### [OpenJev](https://github.com/zhangcy122/OpenJev) · ★40

> **Sibling Model · Open** · `NOASSERTION`

Self-evolving cognitive decision engine and TypeSafe Jev alternative — a System 2→1 decision flywheel with 100% option-order invariance and a typed probabilistic API for open LLMs, Laya, and commercial Jev.

- **Key capabilities:** System 2→1 flywheel · order-invariant


---


## ✅ Source verification

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
