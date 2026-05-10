from typing import List
from Process import Process
class Validator:
    @staticmethod
    def validate(processes: List[Process], quantum: int = None) -> None:
        Validator._check_not_empty(processes)
        Validator._check_duplicate_pids(processes)
        Validator._check_negative_arrival(processes)
        Validator._check_non_positive_burst(processes)
        if quantum is not None:
            Validator._check_quantum(quantum)
    @staticmethod
    def _check_not_empty(processes: List[Process]) -> None:
        if not processes:
            raise ValueError("Process list is empty. Add at least one process.")
    @staticmethod
    def _check_duplicate_pids(processes: List[Process]) -> None:
        seen = set()
        for p in processes:
            if p.pid in seen:
                raise ValueError(
                    f"Duplicate PID detected: '{p.pid}'. "
                    "Every process must have a unique PID."
                )
            seen.add(p.pid)
    @staticmethod
    def _check_negative_arrival(processes: List[Process]) -> None:
        for p in processes:
            if p.arrival < 0:
                raise ValueError(
                    f"Process '{p.pid}' has a negative arrival time ({p.arrival}). "
                    "Arrival time must be ≥ 0."
                )
    @staticmethod
    def _check_non_positive_burst(processes: List[Process]) -> None:
        for p in processes:
            if p.burst <= 0:
                raise ValueError(
                    f"Process '{p.pid}' has an invalid burst time ({p.burst}). "
                    "Burst time must be > 0."
                )
    @staticmethod
    def _check_quantum(quantum: int) -> None:
        if not isinstance(quantum, int) or quantum <= 0:
            raise ValueError(
                f"Invalid quantum value ({quantum}). "
                "Quantum must be a positive integer (> 0)."
            )