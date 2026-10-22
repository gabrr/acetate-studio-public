# Acetate Studio

A workspace for turning PDF and CSV financial statements into transactions you can review, classify, and export.

Built with Next.js, React, TypeScript, Tailwind CSS, and Mantine. Supabase handles authentication; the TRX Classifier backend handles uploads and live processing. Chats and review edits are saved in your browser. The conversation agent is not connected yet; Home charts are illustrative.

Browser support: Chrome/Edge 116+, Firefox 124+, and Safari/iOS 17.4+. Older browsers are not supported for now.

## Run locally

Use Node.js 24. Copy `.env.example` to `.env.local` and fill in your backend and Supabase settings.

```sh
nvm use
npm ci
npm run dev
```

Checks: `npm test`, `npm run typecheck`, `npm run build -- --webpack`.

## Screenshots

New Chat

![New Chat workspace](./new-chat.png)

Home — illustrative charts

![Home dashboard](./home.png)

## Documentation

[Structure](Docs/structure.md) · [Authentication](Docs/authentication.md) · [Verification](Docs/verification.md) · [Tech debt](Docs/Tech%20Debt.md)
