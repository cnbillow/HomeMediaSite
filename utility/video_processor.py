import os

from config import is_unix

from concurrent.futures import ThreadPoolExecutor

threadPool = ThreadPoolExecutor(max_workers=1)


def commit_task(video_file, out_file, timeout=None):
    if is_unix:
        python_interp = "python3"
    else:
        python_interp = "python"
    command = '%s "utility/video_process_exe.py" "%s" "%s"' % (python_interp, video_file, out_file)
    print("Task {}-->{} commited.".format(video_file, out_file))
    return threadPool.submit(os.system, command).result(timeout=timeout)
