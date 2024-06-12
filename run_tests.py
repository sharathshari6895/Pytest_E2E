import subprocess
from concurrent.futures import ThreadPoolExecutor
from Utils.file_util import ui_test_file, api_test_file, mobile_test_file,accessibility_test_file


def run_tests(test_file):
    subprocess.run(["pytest", test_file, "--alluredir=./allure_results"])


# Create a ThreadPoolExecutor with 3 worker threads
with ThreadPoolExecutor(max_workers=1) as executor:
    # Submit tasks for each test file
    futures = [
        # executor.submit(run_tests, ui_test_file),
        # executor.submit(run_tests, api_test_file),
        # executor.submit(run_tests, mobile_test_file),
        executor.submit(run_tests, accessibility_test_file)
    ]

    # Wait for all tasks to complete, allowing a timeout for acquiring the lock
    for future in futures:
        try:
            future.result(timeout=3600)  # 1 hour timeout (adjust as needed)
        except Exception as e:
            print(f"An error occurred: {e}")

print("All test files have been executed.")
