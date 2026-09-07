"""Contract & Capability Registry abstraction.

This module defines the Registry Abstraction responsible for version-safe
contract/capability discovery and resolution. It handles Source Representation
Contract, Source Format Contract, Supported Variant Scope, Parser capability,
Detection capability, Required explicit inputs, and Compatibility/Conformance
metadata. Registry does not perform Format Resolution or become the
reproducibility source. Applicable contract/capability versions must later be
pinnable in a resolution snapshot. No register()/get()/list() interface is
defined in M1.
"""


class ContractCapabilityRegistry:
    """Registry Abstraction for version-safe contract/capability discovery and resolution.

    Capabilities include:
    - Source Representation Contract
    - Source Format Contract
    - Supported Variant Scope
    - Parser capability
    - Detection capability
    - Required explicit inputs
    - Compatibility / Conformance metadata

    The registry does not perform Format Resolution or become the reproducibility source.
    Applicable contract/capability versions must later be pinnable in a resolution snapshot.
    No register()/get()/list() interface is defined in M1.
    """
