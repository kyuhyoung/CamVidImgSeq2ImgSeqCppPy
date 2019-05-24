#import numpy as np
from CamVidImgSeq2ImgSeq import camVidImgSeq2ImgSeq
import sys

def main(idx_cam_or_fn_video_or_img_folder, dir_seq):
    return camVidImgSeq2ImgSeq(idx_cam_or_fn_video_or_img_folder, dir_seq)

if __name__ == '__main__':
    if 3 > len(sys.argv):
        print("Usage : python CamVid2ImgSeq.py [camera index / file path of video / directory path of image sequence] [directory of image sequence to save");   exit()
    main(sys.argv[1], sys.argv[2])



