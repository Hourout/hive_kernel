from ipykernel.kernelapp import IPKernelApp
from .kernel import HiveKernel


IPKernelApp.launch_instance(kernel_class=HiveKernel)
