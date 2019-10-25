import argparse
import multiprocessing as mp
import subprocess

from modules.search_files import find_files

IMG_EXTS = ['.png', '.PNG']
OPTIMIZER_OPTS = ['-o7']


def run_optim(image_path):
    subprocess.run(['optipng', image_path] + OPTIMIZER_OPTS)


def main():
    parser = argparse.ArgumentParser(description='Execute OptiPNG to specified directory with multiprocessing')
    parser.add_argument('input', type=str, help='The directory you want to execute')
    parser.add_argument('-j', '--jobs', type=int, default=mp.cpu_count(), help='Maximum jobs to execute (default: Number of CPU cores)')
    args = parser.parse_args()

    images = find_files(args.input, IMG_EXTS)

    jobs = min([len(images), args.jobs])

    with mp.Pool(jobs) as pool:
        pool.map(run_optim, images)


if __name__ == "__main__":
    main()
