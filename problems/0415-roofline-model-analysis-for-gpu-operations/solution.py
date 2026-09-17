def roofline_analysis(peak_gflops: float, peak_bandwidth_gbs: float, operations: list) -> dict:
	"""
	Perform Roofline Model analysis for GPU operations.

	Args:
		peak_gflops: Peak compute throughput in GFLOPS
		peak_bandwidth_gbs: Peak memory bandwidth in GB/s
		operations: List of dicts with keys 'name', 'flops', 'bytes'

	Returns:
		Dict with 'ridge_point' and 'operations' list containing
		per-operation analysis results.
	"""
	ridge_point = peak_gflops / peak_bandwidth_gbs
	ops = []

	for op in operations:
		name = op["name"]
		operational_intensity = op["flops"] / op["bytes"]
		bottleneck = "compute-bound" if operational_intensity >= ridge_point else "memory-bound"
		attainable_gflops = min(peak_gflops, operational_intensity * peak_bandwidth_gbs)
		efficiency = (attainable_gflops / peak_gflops) * 100
		ops.append({
			"name": name,
			"operational_intensity": operational_intensity,
			"attainable_gflops": attainable_gflops,
			"bottleneck": bottleneck,
			"efficiency": efficiency
		})

	return {
		"ridge_point": ridge_point,
		"operations": ops
	}