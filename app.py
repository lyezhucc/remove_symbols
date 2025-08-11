import customtkinter
import tkinter.filedialog as filedialog
import os
import re
import platform
import subprocess

# --- Core Processing Logic ---
def process_file_content(file_path):
    """Reads a file, removes symbols, and saves to a new file with a suffix."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # --- Symbol Removal ---
        content = content.replace('**', '')
        content = content.replace('*', '')
        content = re.sub(r'^#+\s*', '', content, flags=re.MULTILINE)
        content = re.sub(r'^\s*(?:---|————)\s*$\n?', '', content, flags=re.MULTILINE)

        # --- Generate New File Path ---
        base_path, extension = os.path.splitext(file_path)
        new_file_path = f"{base_path}-已删除符号{extension}"

        # --- Write to New File ---
        with open(new_file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, new_file_path # Return the new path on success
    except Exception as e:
        return False, str(e)


# --- GUI Application Class ---
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # --- Window Setup ---
        self.title("Markdown 符号清理工具")
        self.geometry("700x550") # Increased height for new button
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.file_list = []
        self.last_output_folder = None

        # --- Widget Creation ---
        self.top_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.top_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.top_frame.grid_columnconfigure((0, 1, 2), weight=1)

        self.select_files_button = customtkinter.CTkButton(self.top_frame, text="选择文件", command=self.select_files_callback)
        self.select_files_button.grid(row=0, column=0, padx=5, pady=10)

        self.select_folder_button = customtkinter.CTkButton(self.top_frame, text="选择文件夹", command=self.select_folder_callback)
        self.select_folder_button.grid(row=0, column=1, padx=5, pady=10)
        
        self.start_button = customtkinter.CTkButton(self.top_frame, text="开始清理", command=self.start_processing_callback, fg_color="#28a745", hover_color="#218838")
        self.start_button.grid(row=0, column=2, padx=5, pady=10)

        self.textbox = customtkinter.CTkTextbox(self, corner_radius=0)
        self.textbox.grid(row=1, column=0, sticky="nsew", padx=10, pady=0)
        self.textbox.insert("0.0", "已选文件会显示在这里...\n")

        self.bottom_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.bottom_frame.grid(row=2, column=0, sticky="ew", padx=10, pady=5)
        self.bottom_frame.grid_columnconfigure(0, weight=1)

        self.status_label = customtkinter.CTkLabel(self.bottom_frame, text="准备就绪", anchor="w")
        self.status_label.grid(row=0, column=0, sticky="ew", padx=5)

        self.open_folder_button = customtkinter.CTkButton(self.bottom_frame, text="📂 打开所在文件夹", command=self.open_output_folder_callback, width=160)
        self.open_folder_button.grid(row=0, column=1, padx=5)

    # --- Callback Functions ---

    def open_output_folder_callback(self):
        if self.last_output_folder and os.path.isdir(self.last_output_folder):
            system = platform.system()
            try:
                if system == "Windows":
                    subprocess.run(["explorer", self.last_output_folder])
                elif system == "Darwin": # macOS
                    subprocess.run(["open", self.last_output_folder])
                else: # Linux
                    subprocess.run(["xdg-open", self.last_output_folder])
                self.status_label.configure(text=f"已打开文件夹: {self.last_output_folder}")
            except Exception as e:
                self.status_label.configure(text=f"错误: 无法打开文件夹 {e}")
        else:
            self.status_label.configure(text="提示: 请先处理文件，才能打开输出文件夹。")

    def select_files_callback(self):
        files = filedialog.askopenfilenames(title="选择 Markdown 文件", filetypes=([("Markdown 文件", "*.md"), ("所有文件", "*.*")]));
        if files:
            self.file_list.extend(files)
            self.update_textbox()
            self.status_label.configure(text=f"已添加 {len(files)} 个文件。准备就绪。")

    def select_folder_callback(self):
        folder = filedialog.askdirectory(title="选择文件夹")
        if folder:
            md_files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith('.md')]
            if md_files:
                self.file_list.extend(md_files)
                self.update_textbox()
                self.status_label.configure(text=f"在文件夹中找到 {len(md_files)} 个 .md 文件。准备就绪。")
            else:
                self.status_label.configure(text=f"在所选文件夹中没有找到 .md 文件。")

    def start_processing_callback(self):
        if not self.file_list:
            self.status_label.configure(text="错误：未选择任何文件！")
            return

        self.status_label.configure(text="正在处理中...")
        self.last_output_folder = None # Reset before processing
        self.update()

        success_count = 0
        error_count = 0

        for file_path in self.file_list:
            success, result = process_file_content(file_path)
            if success:
                success_count += 1
                if self.last_output_folder is None:
                    self.last_output_folder = os.path.dirname(result)
            else:
                error_count += 1
                print(f"处理 {file_path} 时出错: {result}")

        final_message = f"处理完成！成功处理 {success_count} 个文件。"
        if error_count > 0:
            final_message += f" 处理失败 {error_count} 个文件（详情请见终端）。"
        
        self.status_label.configure(text=final_message)
        self.file_list = []

    def update_textbox(self):
        self.textbox.delete("0.0", "end")
        unique_files = sorted(list(set(self.file_list)))
        if not unique_files:
             self.textbox.insert("0.0", "已选文件会显示在这里...\n")
        else:
            self.textbox.insert("0.0", "准备处理以下文件：\n\n" + "\n".join(unique_files))


# --- Main Execution ---
if __name__ == "__main__":
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")
    
    app = App()
    app.mainloop()
