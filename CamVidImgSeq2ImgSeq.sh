#   image sequence case
#python main.py --cam_or_vid_or_seq=~/data/Visual_Tracker_Benchmark/Boy/img --save_dir=result_seq/boy --frm_start=0 --margin_lrtb=0,0,150,0 --shift_xy=0.0,1.0
#
#   camera case
#python main.py --cam_or_vid_or_seq=0 --save_dir=result_seq --frm_start=0 --margin_lrtb=0,0,150,0 --shift_xy=0.0,1.0 
python main.py --cam_or_vid_or_seq=1 --save_dir=result_seq
#
#   video file case
#python main.py --cam_or_vid_or_seq=~/data/ucf_crime/Normal_Videos_for_Event_Recognition/Normal_Videos_913_x264.mp4 --save_dir=result_seq --frm_start=0 --margin_lrtb=0,0,150,0 --shift_xy=0.0,1.0 

