# Spotify Daily Recommendation

A personal recommendation engine built with Python, Last.fm, and LLMs to curate daily Spotify playlists based on user listening history and preferences.

Backend that syncs your recently played tracks from Spotify to PostgreSQL and fetches track recommendations from Last.fm.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) and Docker Compose
- [Spotify](https://developer.spotify.com/dashboard) app (Client ID & Secret)
- [Last.fm](https://www.last.fm/api/account/create) API key

## Quick start

1. **Clone and enter the project**
   ```bash
   cd spotify-recommendation-assistant
   ```

2. **Create environment file**
   ```bash
   copy .env.example .env
   ```
   Edit `.env` and set:
   - `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB` — database credentials
   - `SPOTIFY_CLIENT_ID`, `SPOTIFY_CLIENT_SECRET` — from your Spotify app; set redirect URI to `http://127.0.0.1:8000/callback`
   - `LASTFM_API_KEY`, `LASTFM_API_SECRET` — from your Last.fm API account

3. **Run with Docker Compose**
   ```bash
   docker compose up --build -d
   ```
   - Backend: http://localhost:8000  
   - PostgreSQL: `localhost:5432` (use the same user/password/db as in `.env`)


## Environment variables

| Variable | Description |
|----------|-------------|
| `POSTGRES_USER` | PostgreSQL username |
| `POSTGRES_PASSWORD` | PostgreSQL password |
| `POSTGRES_DB` | PostgreSQL database name |
| `SPOTIFY_CLIENT_ID` | Spotify app client ID |
| `SPOTIFY_CLIENT_SECRET` | Spotify app client secret |
| `SPOTIFY_REDIRECT_URI` | OAuth redirect (e.g. `http://127.0.0.1:8000/callback`) |
| `LASTFM_API_KEY` | Last.fm API key |
| `LASTFM_API_SECRET` | Last.fm API secret (optional for basic calls) |




