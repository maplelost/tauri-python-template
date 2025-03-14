# Tauri + Vue + Python 桌面应用模板

这是一个集成了 Tauri、Vue 3 和 Python 后端的桌面应用程序模板。该模板允许您使用 Vue 构建前端 UI，使用 Rust/Tauri
创建跨平台桌面应用程序，并使用 Python 处理后端逻辑。

## 技术栈

- **前端**: Vue 3 + TypeScript
- **桌面框架**: Tauri 2.0 (Rust)
- **后端**: Python (FastAPI)

## 项目结构

```plaintext
├── src/ # Vue前端代码
├── src-tauri/ # Tauri/Rust代码
├── python/ # Python后端代码
└── public/ # 静态资源
```

## 功能特性

- 跨平台桌面应用支持 (Windows, macOS, Linux)
- Vue 3 + TypeScript提供现代化前端开发体验
- Python后端通过FastAPI提供API接口
- Tauri提供安全、轻量的桌面应用包装
- 应用关闭时自动停止Python进程

## 环境要求

- Node.js 16+
- Rust 1.70+
- Python 3.8+
- [Tauri系统依赖](https://tauri.app/v1/guides/getting-started/prerequisites)

## 安装

### 1. 克隆仓库

```bash
git clone https://github.com/yourusername/tauri-vue-python-template.git
cd tauri-vue-python-template
````

### 2. 安装前端依赖

```bash
npm install
```

### 3. 安装 Python 依赖

```bash
pip install -r requirements.txt
```

## 开发

### 开发模式

```bash
npm run build:sidecar-winos
# npm run build:sidecar-macos
# npm run build:sidecar-linux
npm run tauri dev
```

此命令将启动:

- Vite 开发服务器 (Vue 前端)
- Tauri 应用程序
- Python FastAPI 服务器 (通过 Tauri sidecar 自动启动)

### 构建应用

```bash
npm run tauri build
```

这将创建一个生产就绪的桌面应用程序，包含打包的 Python 环境。

## 工作原理

1. 应用启动时，Tauri (Rust) 会自动启动 Python 后端作为 sidecar 进程
2. Vue 前端通过 HTTP 与 Python FastAPI 后端通信 (端口 8008)
3. 应用关闭时，所有进程会被自动清理

## 许可

MIT
