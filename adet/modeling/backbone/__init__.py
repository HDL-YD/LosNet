from .fpn import build_fcos_resnet_fpn_backbone, build_fcos_mobilenetV3small_fpn_backbone
from .vovnet import build_vovnet_fpn_backbone, build_vovnet_backbone
from .dla import build_fcos_dla_fpn_backbone
from .resnet_lpf import build_resnet_lpf_backbone
from .bifpn import build_fcos_resnet_bifpn_backbone
from .squeezenet1_1 import build_fcos_squeezenet1_1_fpn_backbone
from .shufflenetV2x0_5 import build_fcos_shufflenetV2x0_5_fpn_backbone
from .CSPdarknet53 import build_fcos_CSPdarknet53_fpn_backbone
from .mnasnet0_5 import build_fcos_mnasnet0_5_fpn_backbone
from .efficientnetb0 import build_fcos_efficientnetb0_fpn_backbone
from .peleenet import build_fcos_peleenet_fpn_backbone
from .regnet200M import build_fcos_regnet200M_fpn_backbone
from .mobilenet import build_fcos_mobilenetV2_fpn_backbone
