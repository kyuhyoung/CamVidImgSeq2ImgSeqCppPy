import os
import cv2

def is_this_existing_directory(path_dir):
    #return os.path.isdir(path_dir) 
    #print('os.path.expanduser(path_dir) : ', os.path.expanduser(path_dir)) 
    return os.path.isdir(os.path.expanduser(path_dir)) 

def is_video_file(fn): 
    ext = (".3g2", ".3gp", ".asf", ".asx", ".avi", ".flv", ".m2ts", ".mkv", ".mov", ".mp4", ".mpg", ".mpeg", ".rm", ".swf", ".vob", ".wmv")
    '''
    print('fn : ', fn); #exit()
    if fn.endswith(ext):
        print('this is video file')
    else:
        print('this is NOT video file')
    exit()      
    '''
    return fn.endswith(ext)

def init_cam(idx_cam_or_video_path):
    if is_video_file(idx_cam_or_video_path):
        path_video = idx_cam_or_video_path 
        #print('this is video file : ', path_video)
        kam = cv2.VideoCapture(path_video)                          
        if kam is None or not kam.isOpened():
            print('Unable to open video file at : ', path_video);   exit()
    else:
        idx_cam = int(idx_cam_or_video_path) 
        print('this is camera index at : ', idx_cam)
        kam = cv2.VideoCapture(idx_cam)
        if kam is None or not kam.isOpened():
            print('Unable to open camera with index : ', idx_cam);   exit()

    print('Camera : {} is opened'.format(id_cam)); #exit()
    w_h_cam = (int(kam.get(cv2.CAP_PROP_FRAME_WIDTH)), int(kam.get(cv2.CAP_PROP_FRAME_HEIGHT))) # float
    return kam, w_h_cam   

def extract_file_extension(path_file, with_dot):
    extension_with_dot = os.path.splitext(path_file)
    return extension_with_dot if with_dot else extension_with_dot.split('.')[-1] 



def is_image_file(fn): 
    ext = (".bmp", ".ppm", ".png", ".gif", ".jpg", ".jpeg", ".tif", ".pgm")
    return fn.endswith(ext)


def get_list_of_file_path_under_1st_with_2nd_extension(direc, ext = ''):
    
    li_path_total = []
    is_extension_given = is_this_empty_string(ext)
    for dirpath, dirnames, filenames in os.walk(direc):
        n_file_1 = len(filenames)
        if n_file_1:
            if is_extension_given:
                li_path = [os.path.join(dirpath, f) for f in filenames if f.lower().endswith(ext.lower())]
            else:
                li_path = [os.path.join(dirpath, f) for f in filenames]
            n_file_2 = len(li_path)
            if n_file_2:
                li_path_total += li_path
    #print('li_path_total : ', li_path_total);   exit()
    return sorted(li_path_total)



def is_this_empty_string(strin):
    return (strin in (None, '')) or (not strin.stip())


def get_list_of_image_path_under_this_directory(dir_img, ext = ''):
    li_fn_img = get_list_of_file_path_under_1st_with_2nd_extension(dir_img, ext)
    if is_this_empty_string(ext):
        li_fn_img = [fn for fn in li_fn_img if is_image_file(fn)]
    return sorted(li_fn_img)


def mkdir_if_not_exist(path_dir):
    is_newly_made = False
    if not os.path.exists(path_dir):
        os.makedirs(path_dir)
        is_newly_made = True
    return is_newly_made



def get_exact_file_name_from_path(str_path):
    return os.path.splitext(os.path.basename(str_path))[0]

def crop_image(im_bgr, xy_previous, xy_shift, wh_cropped): 
# shift x : '+' means from left to right
#           '-' means from right to left
# shift y : '+' means from top to bottom
#           '-' means from bottom to top
    is_x_bouncing, is_y_bouncing = False, False;
    h_ori, w_ori = im_bgr.shape[:2]
    x_prev, y_prev = xy_previous;   w_cropped, h_cropped = wh_cropped;  x_shift, y_shift = xy_shift
    
    x_cropped = x_prev + x_shift
    if x_cropped < 0:
        x_cropped = float(0)
        is_x_bouncing = True
    if x_cropped + w_cropped > w_ori:
        x_cropped = float(w_ori - w_cropped)
        is_x_bouncing = True

    y_cropped = y_prev + y_shift
    if y_cropped < 0:
        y_cropped = float(0)
        is_y_bouncing = True
    if y_cropped + h_cropped > h_ori:
        y_cropped = float(h_ori - h_cropped)
        is_y_bouncing = True

    xy_previous = [x_cropped, y_cropped]
    if is_x_bouncing:
        xy_shift[0] *= -1.0
    if is_y_bouncing:
        xy_shift[1] *= -1.0

    x_cropped_i, y_cropped_i = round_i(x_cropped), round_i(y_cropped)
    im_bgr_cropped = im_bgr[y_cropped_i : y_cropped_i + h_cropped, x_cropped_i : x_cropped_i + w_cropped]
    #cv2.rectangle(im_bgr, (x_cropped_i, y_cropped_i), (x_cropped_i + w_cropped, y_cropped_i + h_cropped), (0, 0, 255), 1);  cv2.imshow('cropped', im_bgr)
    return im_bgr_cropped, xy_previous, xy_shift

def round_i(x):
    return int(round(x))


def camVidImgSeq2ImgSeq(idx_cam_or_fn_video_or_img_folder, dir_seq, idx_frm_start = 0, margin_lrtb=[0, 0, 0, 0], xy_shift=[0, 0]):
    
    idx_frm = idx_frm_start;
    is_this_image_sequence = False
    li_path_img = []
    #cap = cv2.VideoCapture(opt.idx_cam if opt.is_cam else opt.fn_vid)
    if is_this_existing_directory(idx_cam_or_fn_video_or_img_folder):
        #img_folder = os.path.expanduser(idx_cam_or_fn_video_or_img_folder)
        img_folder = idx_cam_or_fn_video_or_img_folder
        li_path_img = get_list_of_image_path_under_this_directory(img_folder)
        is_this_image_sequence = True
    else:
        idx_cam_or_fn_video = idx_cam_or_fn_video_or_img_folder
        cap, wh_cam = init_cam(idx_cam_or_fn_video)
    '''
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
    '''
    mkdir_if_not_exist(dir_seq)
    xy_offset, wh_cropped = None, None
    while(idx_frm < len(li_path_img) if is_this_image_sequence else cap.isOpened()):
        ret = False
        if is_this_image_sequence:
            frame = cv2.imread(li_path_img[idx_frm])
            ret = True  
            id_img = get_exact_file_name_from_path(li_path_img[idx_frm])
        else:
            ret, frame = cap.read()
            id_img = '%05d' % (idx_frm)
        if True == ret:
            if not xy_offset:
                xy_offset = [float(margin_lrtb[0]), float(margin_lrtb[2])]
            if not wh_cropped:
                h_ori, w_ori = frame.shape[:2]
                wh_cropped = [round_i(w_ori - margin_lrtb[0] - margin_lrtb[1]), round_i(h_ori - margin_lrtb[2] - margin_lrtb[3])]  
            frame, xy_offset, xy_shift = crop_image(frame, xy_offset, xy_shift, wh_cropped)
            '''
            frame = cv2.flip(frame,0)
            # write the flipped frame
            out.write(frame)
            '''
            fn_img = os.path.join(dir_seq, id_img + '.bmp')
            print('fn_img : ', fn_img)
            idx_frm += 1
            cv2.imwrite(fn_img, frame)
            cv2.imshow('frame',frame)
            key = cv2.waitKey(1) & 0xFF
            if 27 == key or ord('q') == key:
                break
        else:
            break
    # Release everything if job is finished
    if not is_this_image_sequence:
        cap.release()

    #out.release()
    cv2.destroyAllWindows()

