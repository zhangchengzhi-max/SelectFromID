
import paramiko

# 创建SSH客户端
client = paramiko.SSHClient()

# 设置不进行SSH密钥验证
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接SSH服务器
client.connect('hz.matpool.com', port=26766, username='root', password='4l*5y1pjB4crrQZ]',allow_agent=False)

sftp = client.open_sftp()

local_file_path = 'D:\database_backup\Test'
remote_file_path = '/phd'


sftp.put(local_file_path, remote_file_path)

# 关闭连接
sftp.close()
client.close()
