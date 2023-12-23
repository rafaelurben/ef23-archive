# 2022 - Rafael Urben

from utils import SortingAlgorithm


def bucketsort_func(data, algorithm_for_sorting_buckets=sorted):
    """
    Run the bucketsort alogrithm on the given data.
    """

    mi = min(data)
    ma = max(data)

    # Create bucket amount depending on the length of the list
    # This could be changed, but here it creates buckets of +- size 10
    bucketcount = len(data)//10+1
    buckets = list([] for i in range(bucketcount))
    bucketrange = (ma-mi)/bucketcount+0.000000001

    # Sort elements into buckets
    for elem in data:
        bucketnum = (elem-mi)/bucketrange
        buckets[int(bucketnum)].append(elem)

    # Run the algorithm to sort each bucket
    sortedbuckets = map(algorithm_for_sorting_buckets, buckets)

    # Merge the buckets into a single list
    result = []
    for bucket in sortedbuckets:
        result += bucket

    return result

# Testing


if __name__ == '__main__':
    bucketsort = SortingAlgorithm(bucketsort_func, sorted)

    r = bucketsort.test(20)
    print(r)

    bucketsort.analyze()
