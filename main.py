#import numpy as np
from CamVidImgSeq2ImgSeq import camVidImgSeq2ImgSeq
import os, sys, argparse

#def main(idx_cam_or_fn_video_or_img_folder, dir_seq, str_frm_start, str_margin_l, str_margin_r, str_margin_t, str_margin_b, str_shift_x, str_shift_y):
def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--cam_or_vid_or_seq', type=str, default='', help='camera index / video file path / image sequence directory path')
    parser.add_argument('--save_dir', type=str, default='result_seq', help='path of directory to save result image sequence')
    parser.add_argument('--frm_start', type=int, default=0, help='frame index of image sequence to start to read')
    parser.add_argument('--margin_lrtb', type=str, default='0,0,0,0', help='left, right, top and bottom margin of the first frame for crop process. "0, 0, 0, 0" means no cropping.')
    parser.add_argument('--shift_xy', type=str, default='0.0,0.0', help='x and y shift while cropping. "0.0, 0.0" means no shift')
    parser.add_argument('--rotation', type=str, default='none', choices=['none', 'left', 'right', '180'], help='rotate the (extracted and cropped) mage. "none" means no rotation')
    parser.add_argument('--mirror', type=str, default='none', choices=['none', 'hori', 'vert'], help='Mirror the (extracted, cropped and rotated) image. "none" means no mirroring')
    opt = parser.parse_args()
    print(opt)
    idx_cam_or_fn_video_or_img_folder = os.path.expanduser(opt.cam_or_vid_or_seq)
    dir_save = os.path.expanduser(opt.save_dir)
    frm_start = opt.frm_start
    #margin_lrtb = map(float, opt.margin_lrtb.split(','))
    #xy_shift = map(float, opt.shift_xy.split(','))
    margin_lrtb = list(map(float, opt.margin_lrtb.split(',')))
    xy_shift = list(map(float, opt.shift_xy.split(',')))
    rotation = opt.rotation
    mirror = opt.mirror
    return camVidImgSeq2ImgSeq(idx_cam_or_fn_video_or_img_folder, dir_save, frm_start, margin_lrtb, xy_shift, rotation, mirror)

if __name__ == '__main__':
    '''
    if 10 > len(sys.argv):
        print("Usage : python CamVid2ImgSeq.py [camera index / file path of video / directory path of image sequence] [directory of image sequence to save] [index start frame] [margin left] [margin right] [margin top] [margin bottom] [shift x] [shift y]");   exit()
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8],sys.argv[9])
    '''
    main();
