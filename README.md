# 💅 Nail Recommender — A CLIP-Based Visual Similarity System

### 🧠 Overview
This project investigates how **multimodal embeddings** can be used for **visual similarity and recommendation tasks**, using **nail designs** as the application domain. 

It integrates **computer vision**, **representation learning**, and **interactive hand tracking** to create a lightweight end-to-end recommendation prototype.

Users can:
- Upload or select an image of nail art  
- Use **MediaPipe Landamrks** for live detection in live mode, easier processing 
- Receive **content-based recommendations** using **CLIP embeddings** and **cosine similarity**


---

### ⚙️ System Architecture

**Frontend:**  
- [Next.js](https://nextjs.org/) for the interface and routing  
- [MediaPipe Hands](https://developers.google.com/mediapipe/solutions/vision/hand_landmarker) for real-time hand tracking and overlay  
- Deployed on [Vercel](https://vercel.com/)

**Backend:**  
- [FastAPI](https://fastapi.tiangolo.com/) for the API  
- [OpenAI CLIP](https://github.com/openai/CLIP) for image embeddings  
- [Pillow](https://python-pillow.org/) and [NumPy](https://numpy.org/) for preprocessing and similarity computations  
- Deployed via [Railway](https://railway.app/)  
- Custom dataset of ~100 curated nail design images for similarity retrieval

---

### 🧩 Methodology

1. **Image Embedding:**  
   Each image in the dataset is encoded into a CLIP embedding vector to capture high-level semantic features.

2. **Query Matching:**  
   A user-uploaded image is encoded and compared via **cosine similarity** against the dataset embeddings to retrieve visually similar designs.

3. **Hand Visualization:**  
   The frontend uses **MediaPipe Hands** to detect hand landmarks and overlay recommended designs interactively.

4. **Integration:**  
   Backend and frontend communicate through REST APIs, providing a lightweight, end-to-end recommendation pipeline.

---

### 🧠 Thought Process & Exploration

Before starting this project, I spent about a month researching possible approaches. I knew I would only have around three weeks to actually build it, so efficiency, simplicity, and cost-effectiveness were my priorities. Training a custom model would take too long, so I focused on leveraging existing, well-optimised solutions.

Initially, I explored **YOLOv8** since it’s excellent for detection-based tasks like this. However, given the time and compute constraints, training my own model wasn’t feasible. I then moved on to experimenting with a range of **classical computer vision techniques** and libraries:

- **MediaPipe (backend):** My first idea was to use MediaPipe Hands to detect nail landmarks directly from images. The challenge was that MediaPipe’s image-based model often struggled with static nail photos — it relies on the palm being visible to infer hand structure. Many nail art photos are cropped, angled, or posed in ways that hide the palm, leading to inconsistent detections.

- **Skin Segmentation (HSV Mask):** This approach actually worked surprisingly well at isolating the hand region, but it struggled to distinguish **nails from skin** — especially for nude or skin-toned bases. Anything within the skin-color range was merged together, so nails weren’t being isolated cleanly.

- **Canny Edge Detection:** Useful for structural outlines, but too broad — it highlighted the entire hand instead of focusing on nails.

- **Background Removal (Rembg):** I tested removing the background first and then applying segmentation, but Rembg proved too heavy to deploy efficiently. Additionally, combining it with skin segmentation sometimes caused the background to reappear in detection masks.

At this point, I wrote a **custom OpenCV script** to try a hybrid approach:
- Load an image with a transparent background  
- Detect the hand contour using the alpha channel  
- Convert to HSV and isolate skin-colored areas  
- Identify *non-skin regions* within the hand contour (potential nails)  
- Filter and highlight the nail contours  

It was clever in theory — isolate the hand, remove the skin, and whatever remained should be the nails. Unfortunately, real-world testing exposed a lot of variability in lighting, hand positions, and tones. The method worked occasionally but wasn’t reliable enough to scale.

That’s when I pivoted toward **CLIP embeddings**. I had already been reading about CLIP’s ability to capture visual-semantic relationships, and although it’s commonly used for text–image retrieval, I realised it was also ideal for **image–image similarity**. Instead of detecting nails directly, I could represent entire designs as embeddings and compute **cosine similarity** to recommend visually similar ones.

I paired this with **MediaPipe on the frontend** — using it to overlay nail designs interactively on the user’s hand. This approach was lightweight, effective, and engaging. By combining CLIP’s embedding space for retrieval with MediaPipe’s real-time visualization, I arrived at a system that balanced **accuracy, performance, and user experience**.

---

### 📊 Key Insights

- CLIP embeddings enable **zero-shot aesthetic similarity** retrieval without fine-tuning.  
- Small, curated datasets can yield meaningful recommendations when paired with effective embeddings.  
- MediaPipe enhances interactivity and bridges model outputs to user perception.  
- Iterating between classical CV methods and embeddings highlights trade-offs between **manual feature engineering** and **deep representation learning**.

---

### 🧪 Future Work

- Expand the dataset for broader color, texture, and lighting diversity  
- Fine-tune CLIP embeddings for domain-specific retrieval  
- Incorporate user feedback loops for iterative improvement  
- Explore **diffusion models** or **GANs** for generative nail design  
- Extend to multimodal search (e.g., text-to-nail-style)

---

### 🖼️ Example Results

| Original Image | Segmentation Attempt |
|----------------|----------------------|
| ![Original Image](https://github.com/user-attachments/assets/d8217a67-fa20-4504-b1af-838f9a5adb4f) | ![Segmentation Attempt](https://github.com/user-attachments/assets/438cdd05-2618-4793-9e72-08a9fa5ed81d) |

#### 🔍 Classical CV Experiments — Detection Pipeline Progression

| Original Image | Skin Segmentation & Background Removal | Hand Contour & Nail Detection |
|----------------|----------------------------------------|--------------------------------|
| ![Original Image](https://github.com/user-attachments/assets/37c572b7-57df-4a9e-b05f-f469211a942b) | ![Skin Segmentation + BG Removal](https://github.com/user-attachments/assets/f12e8d76-56fc-4fd8-ba3b-0614fb5001ae) | ![Hand Contour & Nail Detection](https://github.com/user-attachments/assets/8cece112-0cdc-48f3-860b-3d6f8e3645cc) |

> This shows the progression of classical CV experiments: original image → background and skin segmentation → hand contour and final nail detection.

---

### 🚀 Deployment

**Live demo:** [nail-recommender.vercel.app](https://nail-recommender.vercel.app/)  
**Frontend:** `/frontend`  
**Backend:** `/backend`  
(Deployed via Vercel + Railway)

---

### 👩🏽‍💻 Author

**[Sanmi Areoye](https://github.com/Sanmiareoye)**  
Aspiring Computer Vision Researcher | Representation Learning & Generative Models  

This project was developed as part of my preparation for graduate research applications at **MBZUAI**.



