from enum import Enum
from pydantic import BaseModel, ConfigDict, Field


class ProviderTarget(str, Enum):
    COHERE_DIRECT = "cohere/free"
    OPENROUTER_FREE = "openrouter/free"


class Role(str, Enum):
    SYNTAX_ASSISTANT = "Syntax Assistance"
    FEATURE_BUILDER = "Feature Execution"
    ALGORITHMIC_SOUNDNESS = "Algorithmic Soundness"
    DEVOPS_AUTOMATION = "DevOps Automation"


class ModelProfile(BaseModel):
    identifier: str = Field(..., description="OpenRouter model identifier string")
    provider_target: ProviderTarget = Field(
        ..., description="Routing target provider for OpenRouter"
    )
    role: Role = Field(..., description="Agent role and primary duty classification")
    context_tokens: int = Field(..., ge=1, description="Maximum context window token limit")
    max_output_tokens: int = Field(
        default=4096, ge=1, description="Maximum output token limit"
    )
    temperature: float = Field(
        default=0.7, ge=0.0, le=2.0, description="Sampling temperature"
    )
    top_p: float = Field(
        default=0.9, ge=0.0, le=1.0, description="Nucleus sampling threshold"
    )

    model_config = ConfigDict(frozen=True)


COHERE_NORTH_MINI_CODE = ModelProfile(
    identifier="cohere/north-mini-code:free",
    provider_target=ProviderTarget.COHERE_DIRECT,
    role=Role.SYNTAX_ASSISTANT,
    context_tokens=32768,
)

QWEN_2_5_CODER = ModelProfile(
    identifier="openrouter/free",
    provider_target=ProviderTarget.OPENROUTER_FREE,
    role=Role.FEATURE_BUILDER,
    context_tokens=131072,
)

DEEPSEEK_R1 = ModelProfile(
    identifier="openrouter/free",
    provider_target=ProviderTarget.OPENROUTER_FREE,
    role=Role.ALGORITHMIC_SOUNDNESS,
    context_tokens=131072,
)

LLAMA_AUTO_DEBUGGER = ModelProfile(
    identifier="openrouter/free",
    provider_target=ProviderTarget.OPENROUTER_FREE,
    role=Role.DEVOPS_AUTOMATION,
    context_tokens=131072,
)

MODEL_MATRIX: dict[str, ModelProfile] = {
    "cohere_north_mini_code": COHERE_NORTH_MINI_CODE,
    "qwen_2_5_coder": QWEN_2_5_CODER,
    "deepseek_r1": DEEPSEEK_R1,
    "llama_auto_debugger": LLAMA_AUTO_DEBUGGER,
}