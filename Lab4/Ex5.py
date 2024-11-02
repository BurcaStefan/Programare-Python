def validate_dict(rules, d):
    for key, prefix, middle, suffix in rules:
        if key not in d:
            return False
        value = d[key]
        if not value.startswith(prefix):
            return False
        if not value.endswith(suffix):
            return False
        if middle and (middle not in value[1:-1]):
            return False
    return True

s = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
d = {"key1": "come inside, it's too cold out", "key2": "start something middle and end with winter"}
print(validate_dict(s, d))