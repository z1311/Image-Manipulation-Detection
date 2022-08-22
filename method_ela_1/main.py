import torch
import numpy as np
import argparse
from PIL import Image


import level1, ela
from model import IMDModel




def infer(img_path, model, device):
    print("Performing Level 1 analysis...")
    level1.findMetadata(img_path=img_path)

    print("Performing Level 2 analysis...")
    ela.ELA(img_path=img_path)

    img = Image.open("temp/ela_img.jpg")
    img = img.resize((128,128))
    img = np.array(img, dtype=np.float32).transpose(2,0,1)/255.0
    img = np.expand_dims(img, axis=0)

    out = model(torch.from_numpy(img).to(device=device))
    y_pred = torch.max(out, dim=1)[1]

    print("Prediction:",end=' ')
    print("Authentic" if y_pred else "Tampared") # auth -> 1 and tp -> 0





if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Image Manipulation Detection')

    req_args = parser.add_argument_group('Required Args')
    req_args.add_argument('-p', '--path', type=str, metavar='img_path', dest='img_path', required=True, help='Image Path')

    args = parser.parse_args()

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu') #selecting device
    print("Working on",device)

    model_path = "model/model_c1.pth"
    model = torch.load(model_path,map_location='cpu')

    infer(model=model, img_path=args.img_path, device=device)