# diffusion-spectacles

Logiciel de diffusion de spectacles — scaffold MVP
Stack : FastAPI (Python) backend, PostgreSQL, React (TypeScript) frontend, Docker Compose, GitHub Actions CI.

But : gérer programmation, billetterie basique et suivi technique (MVP).

Prérequis
- Docker & docker-compose
- Node 18+, pnpm/npm/yarn
- Python 3.11+

Installation rapide (local)
1. Créer un fichier .env à partir de backend/.env.example et adapter les valeurs.
2. Lancer : docker-compose up --build
3. Backend accessible : http://localhost:8000 (OpenAPI : /docs)
4. Frontend accessible : http://localhost:5173

Structure
- backend/ : FastAPI app (API REST)
- frontend/ : React + Vite UI (TypeScript)
- infra/docker-compose.yml : Postgres + backend + frontend
- schema.sql : schéma initial de base de données
- .github/workflows/ci.yml : CI (tests lint build)

Variables d'environnement importantes
- DATABASE_URL (ex: postgresql://postgres:postgres@db:5432/diffusion)
- SECRET_KEY (JWT secret pour futur usage)
- STRIPE_SECRET (optionnel pour paiements)

Prochaines étapes proposées (après push du code)
- Exécuter les migrations Alembic et initialiser la BDD.
- Générer issues GitHub automatiques à partir de la roadmap MVP.
- Ajouter tests et couvertures.
- Connecter CI / secrets (DATABASE_URL, DOCKERHUB / registry, STRIPE_SECRET).