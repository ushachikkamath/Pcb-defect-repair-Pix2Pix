# 🛠️ PCB Defect Repair and Correction using Pix2Pix GAN

This project demonstrates the use of a **Pix2Pix GAN** for detecting and correcting defects in Printed Circuit Boards (PCBs). The model learns to map from **defective PCB images** to their corresponding **repaired/ground-truth images**, using a supervised image-to-image translation approach.

Developed and tested in **Google Colab**, with a dataset of side-by-side paired images, this project includes:
- Dataset preparation
- Model training (100 epochs)
- Inference on test data
- Pretrained checkpoint
- Deployment via Hugging Face

---

## 📚 Project Summary

- 🧠 **Model**: Pix2Pix GAN (Isola et al.)
- 🖼️ **Input**: Side-by-side images (`[defective | ground-truth]`)
- 📦 **Training Data**: Preprocessed and included in `./data/`
- 📍 **Testing Data**: Placed in `./datasets/Test/test/`
- ⏱️ **Trained**: 100 epochs
- 💾 **Checkpoint**: Provided in `./checkpoints/`
- 🌐 **Hosted on**: Hugging Face

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/pcb-defect-repair-pix2pix.git
cd pcb-defect-repair-pix2pix
```

---

### 2️⃣ Install Requirements

Make sure you have Python ≥3.7 and PyTorch installed.

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Dataset Preparation

Pix2Pix requires paired images where:  
**Left = Defective PCB**  
**Right = Ground-truth (corrected PCB)**

We use the DeepPCB dataset.

```bash
git clone https://github.com/tangsanli5201/DeepPCB.git
python ./data/preprocessing.py
```

It will store the dataset in `./data/`.

---

### 4️⃣ Prepare Test Data

Place your test defective images inside:

```bash
./datasets/Test/test/
```

Make sure the images are resized and aligned correctly (e.g., 256×256).

---

### 5️⃣ Train the Model

Train the Pix2Pix model for 100 epochs:

```bash
python train.py   --dataroot ./data   --name pcb_pix2pix   --model pix2pix   --direction AtoB   --gpu_ids 0   --n_epochs 100
```

Checkpoints will be saved to:

```bash
./checkpoints/pcb_pix2pix/
```

---

### 6️⃣ Test the Model

Run inference using the test dataset:

```bash
python test.py   --dataroot ./datasets/Test   --name pcb_pix2pix   --model pix2pix   --direction AtoB   --gpu_ids 0   --epoch 100
```

Results will be saved in:

```bash
./results/pcb_pix2pix/test_latest/images/
```

---

### 7️⃣ Pretrained Model

Checkpoints are saved in

```bash
./checkpoints/pcb_pix2pix_100_net_G.pth
```

---

### 8️⃣ Deployment

The model is hosted on **Hugging Face Spaces** for online inference. You can use the files in the sample_images folder to test the model live.

[Try the live demo here](https://huggingface.co/spaces/ushavc/PCB_Defect_Detection_and_Correction_using_pix2pix_GAN)

---

### 🙏 Acknowledgements

- Pix2Pix: [junyanz/pytorch-CycleGAN-and-pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix)
- Dataset: [DeepPCB](https://github.com/tangsanli5201/DeepPCB)
- Platform: Google Colab, Hugging Face
