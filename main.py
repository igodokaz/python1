from so import get_jobs as get_so_jobs
from save import save_to_file

so_jobs = get_so_jobs()
jobs = so_jobs
save_to_file(jobs)

