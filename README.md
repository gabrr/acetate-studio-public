# Acetate Studio

[![Live demo](assets/live-demo.svg)](https://studio.acetate.me) [![In development](assets/development.svg)](#the-product) [![Interactive architecture](assets/architecture.svg)](https://gabrr.github.io/acetate-studio-public/classification.html)

**A modern, AI-native personal finance application.**

Upload PDF or CSV statements. Acetate categorizes your transactions so you can explore your finances through visual interfaces and natural language.

[Explore Studio](https://studio.acetate.me) · Author: [Gabriel Welzel](https://gabrr.app)

## The product

Manual categorization takes time. Acetate’s AI workflow achieves **94% accuracy** when categorizing transactions.

- **Import statements:** PDF and CSV.
- **Live progress:** click a file to follow each processing step.
- **Review transactions:** correct uncertain classifications yourself.
- **Financial activity:** fixed, variable, installments, and money movements.
- **Export:** download transactions as CSV.
- **Rich charts:** explore your finances visually. Dashboard previews below use illustrative data.

**Coming next:** learning from your corrections, natural-language Q&A, and food, transport, housing, subscriptions, and custom categories. Later: iMessage, Telegram, and WhatsApp.

### Statement workspace

![Acetate Studio statement workspace](./new-chat.png)

### Charts · preview

![Acetate Studio dashboard with illustrative charts](./home.png)

## Engineering highlights

Designed and built across the interface, AI workflow, backend, and cloud infrastructure.

- **Applied AI:** extraction, classification, confidence scoring, and evaluations.
- **Reliable processing:** background jobs, retries, and checkpoints.
- **Live experience:** streamed progress and recovery after refresh.
- **Data access:** authenticated, user-scoped jobs and results.

## Architecture

### Transaction classification

An illustrative flow from statement extraction to classification, including the research path for uncertain transactions. Example data and confidence values are simulated.

[![Interactive Acetate transaction classification flow](docs/classification.png)](https://gabrr.github.io/acetate-studio-public/classification.html)

*Click the diagram to play the flow, inspect example data, and switch between fitted and enlarged views.*

## Technology

| Layer | Stack |
| --- | --- |
| Interface | <img src="assets/icons/nextdotjs.svg" width="16" height="16" alt=""> Next.js &nbsp; <img src="assets/icons/react.svg" width="16" height="16" alt=""> React &nbsp; <img src="assets/icons/typescript.svg" width="16" height="16" alt=""> TypeScript &nbsp; <img src="assets/icons/mantine.svg" width="16" height="16" alt=""> Mantine &nbsp; <img src="assets/icons/tailwindcss.svg" width="16" height="16" alt=""> Tailwind CSS |
| Backend & data | <img src="assets/icons/python.svg" width="16" height="16" alt=""> Python &nbsp; <img src="assets/icons/fastapi.svg" width="16" height="16" alt=""> FastAPI &nbsp; <img src="assets/icons/postgresql.svg" width="16" height="16" alt=""> PostgreSQL &nbsp; <img src="assets/icons/supabase.svg" width="16" height="16" alt=""> Supabase Auth |
| AI | <img src="assets/icons/langgraph.svg" width="16" height="16" alt=""> LangGraph &nbsp; <img src="assets/icons/googlegemini.svg" width="16" height="16" alt=""> Gemini &nbsp; TypeSafe &nbsp; Docling &nbsp; LangSmith |
| Infrastructure | <img src="assets/icons/googlecloud.svg" width="16" height="16" alt=""> Google Cloud (Run · Tasks · Storage) &nbsp; <img src="assets/icons/docker.svg" width="16" height="16" alt=""> Docker |

Public product showcase. Application source code is private.

Built by Gabriel Welzel · [gabrr.app](https://gabrr.app)
