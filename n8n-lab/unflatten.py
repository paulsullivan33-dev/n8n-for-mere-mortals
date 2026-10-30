import json, sys

def unflatten(s):
    arr = json.loads(s)
    seen = {}
    def ref(x):
        return build(int(x)) if isinstance(x, str) and x.isdigit() else x
    def build(i):
        if i in seen:
            return seen[i]
        v = arr[i]
        if isinstance(v, dict):
            out = {}
            seen[i] = out
            for k, x in v.items():
                out[k] = ref(x)
            return out
        if isinstance(v, list):
            out = []
            seen[i] = out
            for x in v:
                out.append(ref(x))
            return out
        return v
    return build(0)

if __name__ == "__main__":
    raw = json.load(open(sys.argv[1]))["data"]
    d = unflatten(raw["data"])
    rd = d["resultData"]["runData"]
    for node, runs in rd.items():
        items = runs[0]["data"]["main"][0]
        print(f"{node} -> {json.dumps([i['json'] for i in items])}")
    print("lastNodeExecuted:", d["resultData"].get("lastNodeExecuted"))
