import tarfile
import os
import zipfile
from datetime import datetime


def create_tar_archive(source_dir, output_filename=None):
    """
    创建tar.gz压缩包
    
    Args:
        source_dir: 要压缩的目录路径
        output_filename: 输出文件名（可选，默认使用目录名+时间戳）
    """
    if output_filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"styling_learning_log_{timestamp}.tar.gz"
    
    # 确保输出文件有正确的扩展名
    if not output_filename.endswith('.tar.gz'):
        output_filename += '.tar.gz'
    
    try:
        with tarfile.open(output_filename, 'w:gz') as tar:
            tar.add(source_dir, arcname=os.path.basename(source_dir))
        print(f"成功创建tar.gz压缩包: {output_filename}")
        print(f"源目录: {os.path.abspath(source_dir)}")
        print(f"输出文件: {os.path.abspath(output_filename)}")
        return output_filename
    except Exception as e:
        print(f"创建tar.gz压缩包失败: {e}")
        return None


def create_zip_archive(source_dir, output_filename=None):
    """
    创建zip压缩包
    
    Args:
        source_dir: 要压缩的目录路径
        output_filename: 输出文件名（可选，默认使用目录名+时间戳）
    """
    if output_filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"styling_learning_log_{timestamp}.zip"
    
    # 确保输出文件有正确的扩展名
    if not output_filename.endswith('.zip'):
        output_filename += '.zip'
    
    try:
        with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(source_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, start=os.path.dirname(source_dir))
                    zipf.write(file_path, arcname)
        print(f"成功创建zip压缩包: {output_filename}")
        print(f"源目录: {os.path.abspath(source_dir)}")
        print(f"输出文件: {os.path.abspath(output_filename)}")
        return output_filename
    except Exception as e:
        print(f"创建zip压缩包失败: {e}")
        return None


def main():
    """主函数：打包styling_learning_log项目"""
    # 使用当前脚本的目录作为项目目录
    project_dir = os.path.dirname(os.path.abspath(__file__))
    
    print("开始打包styling_learning_log项目...")
    print("=" * 50)
    
    # 创建tar.gz格式
    tar_file = create_tar_archive(project_dir)
    
    print()
    
    # 创建zip格式
    zip_file = create_zip_archive(project_dir)
    
    print("=" * 50)
    
    if tar_file and zip_file:
        print("打包完成！")
        print("文件信息:")
        
        # 显示文件大小
        for file_path in [tar_file, zip_file]:
            if os.path.exists(file_path):
                size_mb = os.path.getsize(file_path) / (1024 * 1024)
                print(f"  - {file_path}: {size_mb:.2f} MB")
    else:
        print("打包失败，请检查错误信息")


if __name__ == "__main__":
    main()

