# --------------------------------------------------------------------
# Copyright (c) iEXBase. All rights reserved.
# Licensed under the MIT License.
# See License.txt in the project root for license information.
# --------------------------------------------------------------------


class Module:
    """Module Class"""

    def __init__(self, legacy) -> None:
        self.legacy = legacy

    @classmethod
    def attach(cls, target, module_name: str = None) -> None:
        if not module_name:
            module_name = cls.__name__.lower()

        if hasattr(target, module_name):
            raise AttributeError(
                "Cannot set {0} module named '{1}'.  The Legacy object "
                "already has an attribute with that name".format(
                    target,
                    module_name,
                )
            )

        if isinstance(target, Module):
            legacy = target.legacy
        else:
            legacy = target

        setattr(target, module_name, cls(legacy))
