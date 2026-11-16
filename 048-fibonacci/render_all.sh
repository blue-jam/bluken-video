#!/usr/bin/env bash

set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_dir="$(cd "${script_dir}/.." && pwd)"
quality="${1:--ql}"

scenes=(
  "001-introduction/scene.py:FibonacciIntroduction"
  "002-matrix-expression/scene.py:FibonacciMatrixExpression"
  "003-diagonalization/scene.py:DiagonalizationIdea"
  "004-eigenvalues/scene.py:FibonacciEigenvalues"
  "005-eigenvectors/scene.py:FibonacciEigenvectors"
  "006-binet-formula/scene.py:DeriveBinetFormula"
  "007-growth-summary/scene.py:FibonacciGrowthSummary"
)

cd "${repo_dir}"

for scene in "${scenes[@]}"; do
  scene_file="${scene%%:*}"
  scene_class="${scene##*:}"

  echo "Rendering ${scene_file} (${scene_class})"
  uv run manim "${quality}" "048-fibonacci/${scene_file}" "${scene_class}"
done

echo "All Fibonacci scenes rendered successfully."
