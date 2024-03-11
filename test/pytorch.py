import shutil
import os
import sys
import torch
import immutabledict
import sentencepiece
import json

print('Python版本：', sys.version)

# 验证PyTorch
print(torch.rand(5, 3))


print("是否可用：", torch.cuda.is_available())       	# 查看GPU是否可用
print("GPU数量：", torch.cuda.device_count())       	# 查看GPU数量
print("torch方法查看CUDA版本：", torch.version.cuda) 	# torch方法查看CUDA版本
# print("GPU索引号：", torch.cuda.current_device())  	# 查看GPU索引号
# print("GPU名称：", torch.cuda.get_device_name(1)) 	# 根据索引号得到GPU名称



workdir = '/Users/ideamac/env/aigc/data/user'

# 模型
# shutil.unpack_archive(workdir + "/gemma/archive.tar.gz", workdir + "/gemma/gemma-2b")
# 辅助工具
# shutil.unpack_archive(workdir + "/gemma_pytorch/gemma_pytorch-main.zip", workdir + "/gemma_pytorch")




tokenizer_path = os.path.join(workdir + '/gemma/gemma-2b-it', 'tokenizer.model')
ckpt_path = os.path.join(workdir + '/gemma/gemma-2b-it', 'gemma-2b-it.ckpt')
sys.path.append(workdir)
sys.path.append(workdir + '/gemma_pytorch')

from gemma_pytorch.gemma.config import get_config_for_2b
from gemma_pytorch.gemma.model import GemmaForCausalLM

model_config = get_config_for_2b()
model_config.tokenizer = tokenizer_path
model_config.quant = False
torch.set_default_dtype(model_config.get_dtype())
# device = torch.device('cuda')
device = torch.device('cpu')
model = GemmaForCausalLM(model_config)
model.load_weights(ckpt_path)
model = model.to(device).eval()

print('启动完成')

print('============================================================')
response = model.generate('你能生成哪些内容？', device = device, output_len = 64,)
print(response)
print('============================================================')
response = model.generate('你有哪些功能？', device = device, output_len = 64,)
print(response)



