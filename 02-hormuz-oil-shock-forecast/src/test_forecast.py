def test_mc_range():
    import json; s=json.load(open("summary.json"))
    assert s["mc_90d_p5"] < s["mc_90d_p50"] < s["mc_90d_p95"]
    print("PASS MC P5<P50<P95")
if __name__=="__main__": test_mc_range()
