# Markdown 符号清理工具

这是一个用户友好的桌面应用程序，旨在帮助您快速、安全地清理 Markdown 文件中不需要的格式符号。

## ✨ 主要功能

- **图形用户界面**：无需接触命令行，所有操作通过点击按钮完成
- **多种选择方式**：支持选择单个文件、多个文件，或整个文件夹进行批量处理
- **智能符号清理**：
  - 删除行内符号: `*`, `**`
  - 精确删除标题符号: `#`, `##`, `###` 等
  - 彻底清理整行分隔符: `---`, `————`，不留多余空行
- **安全无损**：**不会修改您的原始文件**，而是生成带 `-已删除符号` 后缀的新文件
- **一键直达**：清理完成后，可直接点击按钮打开输出文件所在的文件夹
- **文本处理**：支持直接粘贴文本进行处理，并可一键复制结果

## 🚀 快速开始

### 方式一：使用打包应用（推荐）

我们已为您准备好打包的应用程序，开箱即用！

#### macOS 用户
1. 从 `dist/` 文件夹中选择适合的版本：
   - `Markdown-Cleaner-macOS-v2.0.app` - 最新版本（推荐）
   - `Markdown-Cleaner-macOS-v1.0.app` - 轻量版本
2. 双击 `.app` 文件即可运行

#### 其他平台用户
1. 下载 `dist/Markdown-Cleaner-Universal/` 文件夹
2. 双击其中的 `Markdown Cleaner` 可执行文件

### 方式二：从源码运行（高级用户）

<details>
<summary>点击展开源码安装说明</summary>

#### 步骤 1：准备环境

确保您拥有本项目的全部文件 (`app.py`, `requirements.txt` 等)。

#### 步骤 2：创建并激活虚拟环境

```bash
# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境
# macOS/Linux:
source venv/bin/activate
# Windows:
# venv\Scripts\activate
```

#### 步骤 3：安装依赖

```bash
pip install -r requirements.txt
```

#### 步骤 4：运行应用

```bash
python3 app.py
```

</details>

## 📦 应用版本说明

- **v2.0（macOS）**：包含完整功能的最新版本，支持文件和文本处理
- **v1.0（macOS）**：轻量版本，文件体积更小
- **Universal**：跨平台版本，兼容多种操作系统

## 🛠️ 命令行版本

对于喜欢命令行操作的用户，项目还保留了 `remove_symbols.py` 脚本：

```bash
python remove_symbols.py <文件路径>
```

## 🤝 反馈与支持

如遇到任何问题或有改进建议，欢迎提出 Issue 或 Pull Request。