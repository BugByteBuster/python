import argparse
import urllib.request
import gzip
from collections import Counter


def main(architecture, mirror_url):
    """
    1. It takes two arguments: architecture (the architecture of the content index) and mirror_url (the URL of the Debian mirror).
    2. It constructs the URL for the content index file based on the architecture and mirror URL.
    3. It calls download_and_decompress() to download and decompress the content index file.
    4. If the content index is successfully downloaded, it calls analyze_packages() to analyze its contents. Otherwise, it prints an error message.
    """
    architecture = architecture.lower()
    content_index_url = f"{mirror_url}Contents-{architecture}.gz"
    content_index = download_and_decompress(content_index_url)
    if content_index:
        analyze_packages(content_index)
    else:
        print("Failed to download the content index.")


def download_and_decompress(url):
    """
    Avoids saving the gz file locally.

    1. It tries to open the provided URL using urllib.request.urlopen().
    2. It reads the compressed data from the response.
    3. It decompresses the data using gzip.decompress().
    4. It decodes the decompressed data as UTF-8.
    5. It returns the decompressed data as a string.
    """
    try:
        with urllib.request.urlopen(url) as response:
            compressed_data = response.read()
            decompressed_data = gzip.decompress(compressed_data).decode(
                "utf-8"
            )  # decoding to utf-8
            return decompressed_data
    except Exception as e:
        print(f"Error downloading content index: {e}")
        return None


def analyze_packages(content_index):
    """
    1. It takes one argument: content_index (the content index file data as a string).
    2. It initializes a Counter object to count occurrences of package names.
    3. It iterates over each line in the content index, extracting package names and updating the counter with their occurrences.
    4. It retrieves the top 10 most common packages from the counter.
    5. It prints a header for package statistics and then iterates over the top 10 packages, printing their names and file counts.
    """
    package_counts = Counter()
    for line in content_index.splitlines():
        packages = line.split()[-1].split(",")
        package_counts.update(packages)

    top_10_packages = package_counts.most_common(10)
    print("No.\tPackage Name\t\t\t\t\tFile Count")
    for i, (package_name, count) in enumerate(top_10_packages, start=1):
        print(f"{i}.\t{package_name.ljust(50)}{count}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Get package statistics by parsing a Contents Index from a Debian mirror."
    )
    parser.add_argument(
        "arch",
        type=str,
        help="The architecture of the Contents index you would like to parse.",
    )
    parser.add_argument(
        "-m",
        "--mirror_url",
        type=str,
        default="http://ftp.uk.debian.org/debian/dists/stable/main/",
        help="Mirror URL from which to fetch the contents file.",
    )
    args = parser.parse_args()
    main(args.arch, args.mirror_url)
