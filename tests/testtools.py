import subprocess


def run(script):
    result = subprocess.run(f'python3 samples/{script}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result.stdout = result.stdout.decode()
    result.stderr = result.stderr.decode()
    return result
