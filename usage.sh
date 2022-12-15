: << 'END'
#   image sequence case
python main.py --cam_or_vid_or_seq=~/data/Visual_Tracker_Benchmark/Boy/img --save_dir=result_seq/boy --frm_start=0 --margin_lrtb=0,0,150,0 --shift_xy=0.0,1.0
END

: << 'END'
#   camera case
python main.py --cam_or_vid_or_seq=0 --save_dir=result_seq --frm_start=0 --margin_lrtb=0,0,150,0 --shift_xy=0.0,1.0 
#python main.py --cam_or_vid_or_seq=1 --save_dir=result_seq
END
: << 'END'
#   video file case 1
ext=mp4
for id in 1 2 3 4 5 6 7 8 9
do
    #fn_vid=/mnt/d/work/fxgear/rvm_barracuda/Assets/Videos/seq_01_${id}.${ext}
    fn_vid=input_vid/seq_01_${id}.${ext}
    dir_out=canon_png_${id}
    #fn_vid=input_vid/kinect_rgb_${id}.${ext}
    #dir_out=result_seq_kinect_${id}
    python main.py --cam_or_vid_or_seq=${fn_vid} --save_dir=${dir_out}
done
END

#: << 'END'
#   video file case 2
ext=MOV
direc=/mnt/d/data/XRPoster_testvideo_1207
#for id in 5214 5215 5217 5218 5219
for id in 5215 5217 5218 5219
#for id in 5214
do
    aidi=MVI_${id}
    fn_vid=${direc}/video/${aidi}.${ext}
    #for rot in none left right 180
    for rot in right
    do
        #for mirror in none mirror
        for mirror in none
        do
            #dir_out=output/canon_png_${id}
            dir_out=${direc}/img_seq/${aidi}_rot_${rot}_mirror_${mirror}
            python main.py --cam_or_vid_or_seq ${fn_vid} --save_dir ${dir_out} --rotation ${rot} --mirror ${mirror}
        done
    done
done    
#END
