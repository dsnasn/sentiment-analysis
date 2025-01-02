# 使用 Python 官方基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制应用代码到容器中
COPY . /app

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露 Flask 的端口
EXPOSE 5000

# 启动 Flask 应用
CMD ["python", "run.py"]
