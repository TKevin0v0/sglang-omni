# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Any, ClassVar

from sglang_omni.config import EngineStageConfig, PipelineConfig, StageConfig

_PKG = "sglang_omni.models.fun_asr"


class FunASRPipelineConfig(PipelineConfig):

    architecture: ClassVar[str] = "FunAsrNanoForConditionalGeneration"
    architecture_aliases: ClassVar[tuple[str, ...]] = (
        "FunASRNano",
        "FunASRForConditionalGeneration",
    )

    stage_config_types: ClassVar[dict[str, type[StageConfig]]] = {
        "asr": EngineStageConfig,
    }

    model_path: str
    entry_stage: str = "asr"
    stages: list[StageConfig] = [
        EngineStageConfig(
            name="asr",
            process="asr",
            factory=f"{_PKG}.stages.create_sglang_fun_asr_executor",
<<<<<<< HEAD
            factory_args={
                "device": "cuda:0",
                "max_running_requests": 64,
                "max_new_tokens": 200,
                "enable_encoder_torch_compile": False,
                "enable_encoder_cuda_graph": True,
                "async_decode_min_batch_size": 2,
                "prefill_coalesce_requests": 16,
                "prefill_coalesce_wait_ms": 24,
                "prefill_coalesce_when_idle": True,
                "prefill_coalesce_requires_pending_builds": True,
                "prefill_coalesce_after_builds_during_decode": True,
                "enable_pre_lm_encoder": True,
                "pre_lm_cache_max_entries": 4096,
                "pre_lm_cache_size_bytes": 2 * 1024**3,
                "pre_lm_max_batch_size": 8,
                "pre_lm_max_batch_wait_ms": 10,
                "request_build_max_workers": 8,
                "request_build_max_pending": 32,
            },
||||||| parent of 37bfa830 ([Config] Migrate model configs, example YAMLs and launchers to the grouped surface)
            factory_args={
                "device": "cuda:0",
                "max_running_requests": 32,
                "max_new_tokens": 200,
                "enable_encoder_torch_compile": False,
                "enable_encoder_cuda_graph": True,
                "enable_pre_lm_encoder": True,
                "pre_lm_cache_max_entries": 4096,
                "pre_lm_cache_size_bytes": 2 * 1024**3,
                "pre_lm_max_batch_size": 8,
                "pre_lm_max_batch_wait_ms": 4,
                "request_build_max_workers": 8,
                "request_build_max_pending": 16,
            },
=======
>>>>>>> 37bfa830 ([Config] Migrate model configs, example YAMLs and launchers to the grouped surface)
            gpu=0,
            terminal=True,
        )
    ]

    def stage_factory_kwargs(self, stage_name: str) -> dict[str, Any]:
        if stage_name == "asr":
            return {"enable_encoder_cuda_graph": True}
        return {}


EntryClass = FunASRPipelineConfig
