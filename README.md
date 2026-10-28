# Team C: Flood Early Warning

> Risk dashboard from rainfall and river data

**Hack4Haldia'26** is a 3-hour build challenge. This is your starter repository. Build new features on top of it, integrate them, **deploy the working project**, and open a **Pull Request** on this repository. AI tools and open-source / open-weight models are fully allowed.

## The Problem

Flood alerts reach people too late. Build a system that pulls weather/river data, predicts risk per zone and shows it on a map with alerts.

## Must-have (core, do these first)

- [ ] Ingest rainfall / river-level data from an open weather API
- [ ] Train or apply a risk model (scikit-learn or rules + model)
- [ ] Map with zones coloured by risk level
- [ ] Alert list when a threshold is crossed

## Bonus (only after the core works end to end)

- [ ] Scheduled ingestion (cron / background job)
- [ ] Explain predictions (feature importance)
- [ ] Webhook / email alert on high risk
- [ ] Historical trend charts

## Industry-level tech we expect you to use

- scikit-learn / pandas
- REST API design
- Leaflet / map library
- Background scheduler

A toy in-memory demo is not enough. Use real tools (database, auth, queue, model etc.) where it makes sense.

## What is already here

| File | Purpose |
|---|---|
| `index.html` | Starter UI with an API tester. Replace it with your real frontend. |
| `app.py` + `requirements.txt` | **Python / Flask** starter |
| `script.js` + `package.json` | **Node / Express** starter |

Pick **ONE** stack and delete the other, or keep both if you want. Both expose the same endpoints:

| Method | Path | What it should do |
|---|---|---|
| `GET` | `/health` | Already working |
| `GET` | `/api/readings` | Latest readings per zone |
| `POST` | `/api/predict` | Body: features -> {risk, score} |
| `GET` | `/api/alerts` | Active alerts |

All the endpoints above return `501 Not Implemented` until you build them. Add more endpoints if you need.

## Run locally

**Python**
```bash
pip install -r requirements.txt
python app.py        # http://localhost:5000
```

**Node**
```bash
npm install
npm start            # http://localhost:3000
```

Put secrets in a `.env` file. **Never commit API keys.**

## Deploy (required)

Your project must be live on a public URL. Easiest options:
- **Render**: Web Service, connect the repo. Python start command: `gunicorn app:app`. Node: `npm start`.
- Vercel / Railway / Fly.io also fine.

Add the live URL at the top of your PR description.

## Submit

1. Create a branch: `git checkout -b team-c-solution`
2. Commit and push your work.
3. Open a **Pull Request** against `main` of **this** repository.
4. PR description must include: live URL, what you built, tech used, team members.
5. Also submit on the official **MLH platform (OrganizerHQ)**. Instructions will be given at the start of the event.

## Rules

- Teams of 3 to 4. Every member must be present.
- 3 hours total. Commit often.
- AI tools are open. You must still understand and be able to explain your code.

## Judging

Working demo (35%) | Technical depth (25%) | Completeness of core features (20%) | Deployment (10%) | Presentation (10%)

Good luck, build something great!
