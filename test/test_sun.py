import ray
import mp_build.sun as sun
import math

def test_erf_futures():
    futures = sun.erf_futures(100)
    assert len(futures) == 100
    assert all(isinstance(f, ray.ObjectRef) for f in futures)
    results = ray.get(futures)
    assert len(results) == 100
    assert all(isinstance(r, float) for r in results)
    assert all(math.isclose(r, math.erf(i)) for i, r in enumerate(results))

def test_erf_mp():
    result = sun.erf_mp.remote(1)
    assert math.isclose(ray.get(result), 0.8427007929497148)
    
