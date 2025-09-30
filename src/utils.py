import random
import torch


def get_ip_feat(image, ip_image_processor, ip_clip, ip_resampler):
    ip_image_0 = ip_image_processor(image, return_tensors="pt").pixel_values
    ip_image_0 = ip_image_0.to(ip_clip.device)
    with torch.no_grad():
        with torch.cuda.amp.autocast():
            ip_image_1 = ip_clip(ip_image_0, output_hidden_states=True)
            ip_image_features = ip_resampler(ip_image_1.hidden_states[-2])
    return ip_image_features

def get_random_instruction(jsonfile):
    return random.choice(jsonfile)
