Nail Recommender 💅 — A CLIP-Based Visual Similarity System
🧠 Overview

This project explores how multimodal embeddings can enable personalized recommendations for visual content — in this case, nail designs.
Built in under three weeks, it combines computer vision, representation learning, and interactive hand tracking to create a proof-of-concept recommendation engine that feels research-driven yet accessible.

Users can:

Upload or select an image of nail art

Visualize nail designs on their hands using MediaPipe

Receive content-based recommendations using CLIP embeddings and cosine similarity

⚙️ System Architecture

Frontend:

Next.js
 for the interface and routing

MediaPipe Hands
 for real-time hand tracking and alignment

Deployed on Vercel

Backend:

FastAPI
 for the API

OpenAI CLIP
 for image embeddings

Pillow
 and NumPy
 for preprocessing and similarity computations

Deployed via Railway

Small custom dataset (~100 curated nail design images) for similarity retrieval

🧩 Methodology

Image Embedding:
Each image in the dataset is encoded into a CLIP embedding vector.

Query Matching:
A user-uploaded image is also encoded and compared via cosine similarity against the dataset embeddings.

Hand Visualization:
The frontend uses MediaPipe to detect hand landmarks and overlay the top recommendations interactively.

System Integration:
The project is structured as a light monorepo — the backend and frontend live together for simplicity and reproducibility.

📊 Research Motivation

This prototype explores:

The feasibility of zero-shot visual similarity using CLIP embeddings without task-specific fine-tuning.

The potential of interactive recommendation systems that bridge computer vision and user experience.

The role of small, domain-specific datasets in rapid prototyping and concept validation.

While the system is intentionally lightweight, it serves as a mini research sandbox demonstrating end-to-end thinking — from data collection and model choice to interface design and deployment.

🧪 Future Work

Expand the dataset to include broader color, texture, and lighting variations

Fine-tune CLIP embeddings for domain specificity

Integrate user feedback loops for personalized refinement

Experiment with diffusion-based models for generative nail design suggestions

🚀 Deployment

Live demo: nail-recommender.vercel.app

Frontend: /frontend
Backend: /backend
(Deployed via Vercel + Railway)

👩🏽‍💻 Author

Sanmi Areoye

Aspiring ML Researcher | Computer Vision & Generative Models Enthusiast
This project was developed as part of my preparation for graduate research applications at MBZUAI.
