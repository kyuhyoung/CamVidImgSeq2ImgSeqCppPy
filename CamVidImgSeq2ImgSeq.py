import os
import cv2

def is_this_existing_directory(path_dir):
    return os.path.isdir(path_dir) 

def is_video_file(fn): 
    ext = (".3g2", ".3gp", ".asf", ".asx", ".avi", ".flv", ".m2ts", ".mkv", ".mov", ".mp4", ".mpg", ".mpeg", ".rm", ".swf", ".vob", ".wmv")
    return fn.endswith(ext)

def init_cam(id_cam):
    if is_video_file(id_cam):
        #print('this is video file')
        kam = cv2.VideoCapture(id_cam)                          
    else:
        kam = cv2.VideoCapture(int(id_cam))
    if kam is None or not kam.isOpened():
        print('Unable to open camera ID : ', id_cam);   exit()
    print('Camera : {} is opened'.format(id_cam))
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


def camVidImgSeq2ImgSeq(idx_cam_or_fn_video_or_img_folder, dir_seq):
    
    idx_frm = 0
    is_this_image_sequence = False
    li_path_img = []
    #cap = cv2.VideoCapture(opt.idx_cam if opt.is_cam else opt.fn_vid)
    if is_this_existing_directory(idx_cam_or_fn_video_or_img_folder):
        img_folder = idx_cam_or_fn_video_or_img_folder
        li_path_img = get_list_of_image_path_under_this_directory(img_folder)
        is_this_image_sequence = True
    else:
        idx_cam_or_fn_video = idx_cam_or_fn_video_or_img_folder
        cap = init_cam(idx_cam_or_fn_video)
    '''
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
    '''
    mkdir_if_not_exist(dir_seq)
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
    cap.release()
    #out.release()
    cv2.destroyAllWindows()

