import functools

def solution(l):
    def split_version(version):
        return [int(x) for x in version.split('.')]

    def compare_versions(version1, version2):
        v1_split = split_version(version1)
        v2_split = split_version(version2)
        v1_len, v2_len = len(v1_split), len(v2_split)

        for i in range(max(v1_len, v2_len)):
            v1 = v1_split[i] if i < v1_len else 0
            v2 = v2_split[i] if i < v2_len else 0
            if v1 != v2:
                return v1 - v2
        return v1_len - v2_len

    return sorted(l, key=functools.cmp_to_key(compare_versions))

# Test case
l = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]
print(solution(l))  # Output should be ['1.0', '1.0.2', '1.0.12', '1.1.2', '1.3.3']


# Python 2.7 implementation
# def solution(l):
#     def split_version(version):
#         return [int(x) for x in version.split('.')]

#     def compare_versions(version1, version2):
#         v1_split = split_version(version1)
#         v2_split = split_version(version2)
#         v1_len, v2_len = len(v1_split), len(v2_split)

#         for i in range(max(v1_len, v2_len)):
#             v1 = v1_split[i] if i < v1_len else 0
#             v2 = v2_split[i] if i < v2_len else 0
#             if v1 != v2:
#                 return v1 - v2
#         return v1_len - v2_len

#     return sorted(l, cmp=compare_versions)