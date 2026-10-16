# Vehicle Detection and Number Plate Recognition (ANPR) – India

A learning project to detect vehicles in an image and read Indian number plates
(format like `MH 13 AB 1234`).

## Pipeline
1. Input image
2. Detect vehicles with a pretrained YOLO model (car, bus, truck, motorcycle)
3. Detect the number plate inside each vehicle (OpenCV method, then a YOLO plate model)
4. Clean the plate image (crop, resize, grayscale, threshold, straighten)
5. Read the text with OCR (EasyOCR)
6. Fix and check the text using the Indian plate pattern

## Project structure
- `notebooks/` – Jupyter notebooks, one per phase
- `src/` – reusable Python code
- `data/samples/` – a few small public test images
- `data/my_photos/` – my own photos (not uploaded)
- `data/datasets/` – downloaded datasets (not uploaded)
- `models/` – model weights (not uploaded)
- `outputs/` – saved results (not uploaded)

## Setup (Windows)

- py -3.11 -m venv .venv
- venv\Scripts\Activate.ps1
- python -m pip install --upgrade pip
- python -m pip install ipykernel



## Data and privacy
Number plates are personal data. This project uses only public datasets and my own
photos. Private photos, datasets, and model weights are kept out of this repository.

## Progress
- [x] Phase 0: Setup
- [ ] Phase 1: Vehicle detection with pretrained YOLO
- [ ] Phase 2: Classic OpenCV plate detection
- [ ] Phase 3: YOLO plate detector + EasyOCR
- [ ] Phase 4: Text fixing and testing