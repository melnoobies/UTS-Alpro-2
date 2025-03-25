import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
import random
import locale

class WeddingPlannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Wedding Planner App")
        self.root.geometry("800x600")
        self.root.configure(bg="#FFF0F5")  # Light pink background
        
        # App state variables
        self.recommended_vendors = set()
        self.current_frame = None
        self.budget = 0
        self.quality_range = 0
        self.selected_categories = []
        self.selected_vendors = {}
        self.payment_method = ""
        
        # Set locale for number formatting
        locale.setlocale(locale.LC_ALL, '')
        
        # Define vendor categories with their respective vendors
        self.vendor_categories = {
            "Venue": self.generate_vendors("Venue", ["Grand Palace", "Luxury Gardens", "Elite Mansion", "Premium Plaza", "Elegant Hall", 
                                          "Comfort Inn", "Simple Space", "Basic Ballroom", "Budget Venue", "Local Hall"]),
            "Catering": self.generate_vendors("Catering", ["Gourmet Delights", "Premium Taste", "Luxury Bites", "Elite Cuisine", "Fine Dining",
                                            "Good Eats", "Family Kitchen", "Simple Plates", "Budget Meals", "Basic Food"]),
            "Fotografi": self.generate_vendors("Fotografi", ["Elite Captures", "Luxury Lens", "Premium Shots", "Artistic Vision", "High-End Photos",
                                             "Good Memories", "Smile Shots", "Simple Clicks", "Budget Photos", "Basic Pictures"]),
            "MC & Entertainment": self.generate_vendors("MC & Entertainment", ["Luxury Live", "Premium Performers", "Elite Entertainment", "High-End Shows", "Star Hosts",
                                                      "Good Times", "Friendly Hosts", "Simple Acts", "Budget Fun", "Basic Entertainment"]),
            "Makeup & Hairstyling": self.generate_vendors("Makeup & Hairstyling", ["Glamour Touch", "Elite Beauty", "Premium Looks", "Luxury Style", "High-End Makeovers",
                                                       "Pretty Good", "Nice Looks", "Simple Beauty", "Budget Style", "Basic Makeup"]),
            "Undangan & Souvenir": self.generate_vendors("Undangan & Souvenir", ["Luxury Gifts", "Premium Mementos", "Elite Invites", "High-End Souvenirs", "Designer Cards",
                                                       "Good Memories", "Nice Tokens", "Simple Gifts", "Budget Invites", "Basic Souvenirs"]),
            "Transportasi": self.generate_vendors("Transportasi", ["Luxury Fleet", "Premium Cars", "Elite Limousines", "High-End Transport", "Exclusive Rides",
                                                "Comfortable Cars", "Decent Vehicles", "Simple Transport", "Budget Rides", "Basic Cars"]),
            "Kue Pernikahan": self.generate_vendors("Kue Pernikahan", ["Luxury Delights", "Premium Pastries", "Elite Cakes", "Gourmet Creations", "Artisan Bakery",
                                                  "Tasty Treats", "Sweet Moments", "Simple Cakes", "Budget Bakery", "Basic Sweets"]),
            "Wedding Organizer": self.generate_vendors("Wedding Organizer", ["Elite Planners", "Luxury Events", "Premium Coordination", "High-End Organizers", "Exclusive Planning",
                                                     "Good Organization", "Reliable Planners", "Simple Coordination", "Budget Planning", "Basic Organization"]),
            "Videografer": self.generate_vendors("Videografer", ["Cinematic Dreams", "Premium Films", "Elite Videos", "Luxury Productions", "High-End Captures",
                                               "Good Memories", "Nice Films", "Simple Videos", "Budget Recordings", "Basic Videos"])
        }
        
        # Define category priorities (1 is highest priority)
        self.category_priorities = {
            "Venue": 1,
            "Catering": 2,
            "Fotografi": 3,
            "Wedding Organizer": 4,
            "Videografer": 5,
            "MC & Entertainment": 6,
            "Makeup & Hairstyling": 7,
            "Kue Pernikahan": 8,
            "Transportasi": 9,
            "Undangan & Souvenir": 10
        }
        
        # Create and show the welcome frame
        self.show_welcome_frame()
    
    def generate_vendors(self, category, names):
        vendors = []
        # Create vendors with descending quality (5 stars to 0 stars)
        for i, name in enumerate(names):
            quality = 5 - i // 2  # Distributes ratings from 5 down to 0
            # Calculate price based on quality (higher quality = higher price)
            base_price = random.randint(5000000, 10000000)  # Base price between 5-10 million
            price = base_price + (quality * 2000000)  # Each quality star adds 2 million
            
            vendors.append({
                "name": name,
                "category": category,
                "quality": quality,
                "price": price
            })
        return vendors
    
    def show_welcome_frame(self):
        # Welcome frame implementation remains the same...
        if self.current_frame:
            self.current_frame.destroy()
        
        frame = tk.Frame(self.root, bg="#FFF0F5")
        frame.pack(fill="both", expand=True)
        
        # Header
        header_frame = tk.Frame(frame, bg="#FF69B4")  # Hot pink header
        header_frame.pack(fill="x", pady=10)
        
        header_label = tk.Label(header_frame, text="Wedding Planner App", font=("Arial", 24, "bold"), 
                               bg="#FF69B4", fg="white", pady=10)
        header_label.pack()
        
        # Content
        content_frame = tk.Frame(frame, bg="#FFF0F5")
        content_frame.pack(pady=50)
        
        welcome_label = tk.Label(content_frame, text="Selamat Datang di Wedding Planner App!", 
                                font=("Arial", 18), bg="#FFF0F5", pady=20)
        welcome_label.pack()
        
        # Start planning button
        start_button = tk.Button(content_frame, text="Mulai Perencanaan", font=("Arial", 14), bg="#FF69B4", fg="white",
                                padx=20, pady=10, command=self.show_budget_frame)
        start_button.pack(pady=20)
        
        # Footer
        footer_frame = tk.Frame(frame, bg="#FF69B4")
        footer_frame.pack(fill="x", side="bottom")
        
        footer_label = tk.Label(footer_frame, text="© 2025 Wedding Planner App", font=("Arial", 10), 
                               bg="#FF69B4", fg="white", pady=5)
        footer_label.pack()
        
        self.current_frame = frame
    
    def show_budget_frame(self):
        if self.current_frame:
            self.current_frame.destroy()
        
        frame = tk.Frame(self.root, bg="#FFF0F5")
        frame.pack(fill="both", expand=True)
        
        # Header
        header_frame = tk.Frame(frame, bg="#FF69B4")
        header_frame.pack(fill="x", pady=10)
        
        header_label = tk.Label(header_frame, text="Set Your Budget", font=("Arial", 24, "bold"), 
                               bg="#FF69B4", fg="white", pady=10)
        header_label.pack()
        
        # Content
        content_frame = tk.Frame(frame, bg="#FFF0F5")
        content_frame.pack(pady=50)
        
        budget_label = tk.Label(content_frame, text="Masukkan Budget Pernikahan Anda (Rp):", 
                               font=("Arial", 14), bg="#FFF0F5", pady=10)
        budget_label.pack()
        
        # Budget Entry Frame with Label
        budget_entry_frame = tk.Frame(content_frame, bg="#FFF0F5")
        budget_entry_frame.pack(pady=10)
        
        # Add Rp label
        rp_label = tk.Label(budget_entry_frame, text="Rp", font=("Arial", 14), bg="#FFF0F5")
        rp_label.pack(side="left", padx=(0, 5))
        
        # Create formatted Entry with trace
        self.budget_var = tk.StringVar()
        self.budget_var.trace_add("write", self.format_budget_entry)
        
        self.budget_entry = tk.Entry(budget_entry_frame, font=("Arial", 14), width=20, 
                                   textvariable=self.budget_var, justify="right")
        self.budget_entry.pack(side="left")
        
        # Buttons frame
        buttons_frame = tk.Frame(content_frame, bg="#FFF0F5")
        buttons_frame.pack(pady=20)
        
        next_button = tk.Button(buttons_frame, text="Selanjutnya", font=("Arial", 12), bg="#FF69B4", fg="white",
                               padx=20, pady=10, command=self.validate_budget)
        next_button.pack(side="left", padx=10)
        
        back_button = tk.Button(buttons_frame, text="Kembali", font=("Arial", 12), bg="#888888", fg="white",
                               padx=20, pady=10, command=self.show_welcome_frame)
        back_button.pack(side="left", padx=10)
        
        # Footer
        footer_frame = tk.Frame(frame, bg="#FF69B4")
        footer_frame.pack(fill="x", side="bottom")
        
        footer_label = tk.Label(footer_frame, text="© 2025 Wedding Planner App", font=("Arial", 10), 
                               bg="#FF69B4", fg="white", pady=5)
        footer_label.pack()
        
        self.current_frame = frame
    
    def format_budget_entry(self, *args):
        """Format the budget entry as the user types"""
        current_text = self.budget_var.get()
        
        # Remove existing formatting (dots, commas) and non-digits
        digits_only = ''.join(filter(str.isdigit, current_text))
        
        # Prevent the callback from triggering again when we set the value
        self.budget_var.trace_remove("write", self.budget_var.trace_info()[0][1])
        
        if digits_only:
            # Menambahkan titik sebagai pemisah ribuan setiap tiga digit dari kanan
            formatted_text = ""
            for i, digit in enumerate(reversed(digits_only)):
                if i > 0 and i % 3 == 0:
                    formatted_text = "." + formatted_text
                formatted_text = digit + formatted_text
            
            self.budget_var.set(formatted_text)
        else:
            self.budget_var.set("")
        
        # Re-add the trace
        self.budget_var.trace_add("write", self.format_budget_entry)
    
    def validate_budget(self):
        try:
            # Get the budget value without formatting
            budget_str = self.budget_var.get().replace(".", "")
            
            if not budget_str:
                messagebox.showerror("Error", "Masukkan angka yang valid")
                return
                
            budget = int(budget_str)
            if budget <= 0:
                messagebox.showerror("Error", "Budget harus lebih dari 0")
                return
            
            self.budget = budget
            self.show_quality_frame()
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid")
    
    def show_quality_frame(self):
        if self.current_frame:
            self.current_frame.destroy()
        
        frame = tk.Frame(self.root, bg="#FFF0F5")
        frame.pack(fill="both", expand=True)
        
        # Header
        header_frame = tk.Frame(frame, bg="#FF69B4")
        header_frame.pack(fill="x", pady=10)
        
        header_label = tk.Label(header_frame, text="Select Quality Range", font=("Arial", 24, "bold"), 
                              bg="#FF69B4", fg="white", pady=10)
        header_label.pack()
        
        # Content
        content_frame = tk.Frame(frame, bg="#FFF0F5")
        content_frame.pack(pady=50)
        
        quality_label = tk.Label(content_frame, text="Pilih Range Kualitas Vendor:", 
                                font=("Arial", 14), bg="#FFF0F5", pady=10)
        quality_label.pack()
        
        quality_desc = tk.Label(content_frame, text="(5 = Kualitas Tertinggi, 1 = Kualitas Terendah)", 
                              font=("Arial", 12), bg="#FFF0F5")
        quality_desc.pack(pady=(0, 20))
        
        # Quality selection
        self.quality_var = tk.IntVar(value=3)  # Default to middle quality
        
        quality_frame = tk.Frame(content_frame, bg="#FFF0F5")
        quality_frame.pack(pady=10)
        
        for i in range(1, 6):
            rb = tk.Radiobutton(quality_frame, text=f"{i} ★", font=("Arial", 14), variable=self.quality_var, 
                              value=i, bg="#FFF0F5", indicatoron=0, width=5, pady=10,
                              selectcolor="#FF69B4", foreground="black")
            rb.pack(side="left", padx=5)
        
        # Buttons frame
        buttons_frame = tk.Frame(content_frame, bg="#FFF0F5")
        buttons_frame.pack(pady=20)
        
        next_button = tk.Button(buttons_frame, text="Selanjutnya", font=("Arial", 12), bg="#FF69B4", fg="white",
                              padx=20, pady=10, command=self.save_quality_selection)
        next_button.pack(side="left", padx=10)
        
        back_button = tk.Button(buttons_frame, text="Kembali", font=("Arial", 12), bg="#888888", fg="white",
                              padx=20, pady=10, command=self.show_budget_frame)
        back_button.pack(side="left", padx=10)
        
        # Footer
        footer_frame = tk.Frame(frame, bg="#FF69B4")
        footer_frame.pack(fill="x", side="bottom")
        
        footer_label = tk.Label(footer_frame, text="© 2025 Wedding Planner App", font=("Arial", 10), 
                              bg="#FF69B4", fg="white", pady=5)
        footer_label.pack()
        
        self.current_frame = frame

    def save_quality_selection(self):
        self.quality_range = self.quality_var.get()
        self.show_category_selection_frame()
    
    def show_category_selection_frame(self):
        if self.current_frame:
            self.current_frame.destroy()
        
        frame = tk.Frame(self.root, bg="#FFF0F5")
        frame.pack(fill="both", expand=True)
        
        # Header
        header_frame = tk.Frame(frame, bg="#FF69B4")
        header_frame.pack(fill="x", pady=10)
        
        header_label = tk.Label(header_frame, text="Select Vendor Categories", font=("Arial", 24, "bold"), 
                               bg="#FF69B4", fg="white", pady=10)
        header_label.pack()
        
        # Content
        content_frame = tk.Frame(frame, bg="#FFF0F5")
        content_frame.pack(pady=30)
        
        category_label = tk.Label(content_frame, text="Pilih Kategori Vendor yang Anda Inginkan:", 
                                 font=("Arial", 14), bg="#FFF0F5", pady=10)
        category_label.pack()
        
        # Category selection checkboxes
        categories_frame = tk.Frame(content_frame, bg="#FFF0F5")
        categories_frame.pack(pady=10)
        
        self.category_vars = {}
        
        # Create two columns of checkboxes
        left_frame = tk.Frame(categories_frame, bg="#FFF0F5")
        left_frame.pack(side="left", padx=20)
        
        right_frame = tk.Frame(categories_frame, bg="#FFF0F5")
        right_frame.pack(side="left", padx=20)
        
        categories = list(self.vendor_categories.keys())
        mid_point = len(categories) // 2
        
        # Left column
        for category in categories[:mid_point]:
            var = tk.BooleanVar()
            self.category_vars[category] = var
            
            cb = tk.Checkbutton(left_frame, text=category, variable=var, font=("Arial", 12), 
                               bg="#FFF0F5", padx=10, pady=5)
            cb.pack(anchor="w", pady=5)
        
        # Right column
        for category in categories[mid_point:]:
            var = tk.BooleanVar()
            self.category_vars[category] = var
            
            cb = tk.Checkbutton(right_frame, text=category, variable=var, font=("Arial", 12), 
                               bg="#FFF0F5", padx=10, pady=5)
            cb.pack(anchor="w", pady=5)
        
        # Budget info
        budget_info = tk.Label(content_frame, text=f"Budget: Rp. {self.format_number(self.budget)} • Quality Level: {self.quality_range}★", 
                              font=("Arial", 12, "bold"), bg="#FFF0F5", pady=10)
        budget_info.pack(pady=10)
        
        # Buttons frame
        buttons_frame = tk.Frame(content_frame, bg="#FFF0F5")
        buttons_frame.pack(pady=20)
        
        next_button = tk.Button(buttons_frame, text="Selanjutnya", font=("Arial", 12), bg="#FF69B4", fg="white",
                               padx=20, pady=10, command=self.save_category_selection)
        next_button.pack(side="left", padx=10)
        
        back_button = tk.Button(buttons_frame, text="Kembali", font=("Arial", 12), bg="#888888", fg="white",
                               padx=20, pady=10, command=self.show_quality_frame)
        back_button.pack(side="left", padx=10)
        
        # Footer
        footer_frame = tk.Frame(frame, bg="#FF69B4")
        footer_frame.pack(fill="x", side="bottom")
        
        footer_label = tk.Label(footer_frame, text="© 2025 Wedding Planner App", font=("Arial", 10), 
                               bg="#FF69B4", fg="white", pady=5)
        footer_label.pack()
        
        self.current_frame = frame

    def save_category_selection(self):
        # Pastikan self.recommended_vendors tersedia
        if not hasattr(self, "recommended_vendors"):
            self.recommended_vendors = set()
        
        selected = [category for category, var in self.category_vars.items() if var.get()]
        
        if not selected:
            messagebox.showerror("Error", "Silakan pilih minimal satu kategori vendor")
            return

        # Check if budget is sufficient for the selected categories and quality
        estimated_cost = self.estimate_categories_cost(selected)

        # Jika anggaran tidak cukup, coba optimasi vendor selection
        if estimated_cost > self.budget:
            optimized_result = self.optimize_vendor_selection(selected)
            
            if optimized_result:
                warning_message = ("Anggaran Anda mungkin tidak mencukupi untuk semua kategori dan kualitas yang dipilih.\n\n"
                                "Kami telah menyarankan beberapa perubahan untuk menyesuaikan dengan budget Anda:")

                if optimized_result["quality_change"]:
                    warning_message += f"\n\n• Kualitas diturunkan dari {self.quality_range}★ menjadi {optimized_result['new_quality']}★"

                if optimized_result["removed_categories"]:
                    warning_message += "\n\n• Kategori yang tidak diprioritaskan:"
                    for cat in optimized_result["removed_categories"]:
                        warning_message += f"\n  - {cat}"

                warning_message += (f"\n\nPerkiraan biaya awal: Rp. {self.format_number(estimated_cost)}"
                                    f"\nPerkiraan biaya setelah optimasi: Rp. {self.format_number(optimized_result['new_cost'])}"
                                    f"\nBudget Anda: Rp. {self.format_number(self.budget)}")

                continue_with_optimization = messagebox.askyesno("Rekomendasi Optimasi Budget", warning_message + "\n\nApakah Anda ingin melanjutkan dengan rekomendasi ini?")

                if continue_with_optimization:
                    self.quality_range = optimized_result["new_quality"]
                    selected = optimized_result["new_categories"]

                    # Hitung vendor termurah per kategori dengan logika yang sama seperti perkiraan biaya
                    chosen_vendor_names = []
                    for cat in selected:
                        matching_vendors = [v for v in self.vendor_categories[cat]
                                            if self.quality_range - 1 <= v["quality"] <= self.quality_range + 1]
                        if matching_vendors:
                            cheapest = min(matching_vendors, key=lambda x: x["price"])
                        else:
                            cheapest = min(self.vendor_categories[cat], key=lambda x: abs(x["quality"] - self.quality_range))
                        chosen_vendor_names.append(cheapest["name"])
                    self.recommended_vendors = set(chosen_vendor_names)

                    # Untuk memunculkan Notifikasi
                    messagebox.showinfo("Perubahan Diterapkan", 
                                        "Perubahan telah diterapkan. Anda akan melanjutkan dengan vendor rekomendasi seperti pada perkiraan biaya setelah optimasi.")
                else:
                    self.recommended_vendors = set()

        else:
            # Jika anggaran cukup, hitung vendor termurah per kategori yang dipilih
            chosen_vendor_names = []
            for cat in selected:
                matching_vendors = [v for v in self.vendor_categories[cat]
                                    if self.quality_range - 1 <= v["quality"] <= self.quality_range + 1]
                if matching_vendors:
                    cheapest = min(matching_vendors, key=lambda x: x["price"])
                else:
                    cheapest = min(self.vendor_categories[cat], key=lambda x: abs(x["quality"] - self.quality_range))
                chosen_vendor_names.append(cheapest["name"])
            self.recommended_vendors = set(chosen_vendor_names)

        self.show_budget_breakdown(selected, self.estimate_categories_cost(selected))
        self.selected_categories = selected
        self.show_vendor_selection_frame()

    def estimate_categories_cost(self, categories, quality=None):
        """Estimate the minimum cost for selected categories based on quality"""
        if quality is None:
            quality = self.quality_range
            
        total_cost = 0
        
        # For each category, get the vendors within quality range and find the cheapest
        for category in categories:
            # Get vendors that match our quality range (quality +/- 1)
            matching_vendors = [vendor for vendor in self.vendor_categories[category] 
                               if quality - 1 <= vendor["quality"] <= quality + 1]
            
            if matching_vendors:
                # Add the cheapest vendor's price
                cheapest_vendor = min(matching_vendors, key=lambda x: x["price"])
                total_cost += cheapest_vendor["price"]
            else:
                # If no vendors match the quality range, use the closest quality
                closest_vendor = min(self.vendor_categories[category], 
                                    key=lambda x: abs(x["quality"] - quality))
                total_cost += closest_vendor["price"]
        
        return total_cost
    
    def optimize_vendor_selection(self, selected_categories):
        """Gunakan backtracking untuk mengoptimalkan pemilihan vendor berdasarkan anggaran"""
        original_quality = self.quality_range # Menyimpan nilai kualitas asli yang dipilih pengguna ke dalam variabel original_quality.
        original_categories = selected_categories.copy() # Membuat salinan dari daftar kategori yang dipilih agar dapat digunakan sebagai referensi saat mencoba alternatif tanpa mengubah daftar asli.
        
        # Pastikan variabel recommended_vendors tersedia
        self.recommended_vendors = set() # sebagai himpunan kosong untuk menyimpan vendor rekomendasi hasil optimasi.

        def get_cheapest_vendors(categories, quality):
            cheapest_names = []
            for cat in categories:
                # Ambil vendor dalam range quality
                matching_vendors = [v for v in self.vendor_categories[cat] 
                                    if quality - 1 <= v["quality"] <= quality + 1] # sebagai himpunan kosong untuk menyimpan vendor rekomendasi hasil optimasi.
                
                # Jika ditemukan vendor dalam rentang tersebut, pilih vendor dengan harga terendah
                if matching_vendors:
                    cheapest = min(matching_vendors, key=lambda x: x["price"])
                    cheapest_names.append(cheapest["name"]) 
                else:
                    # Jika tidak ada yang persis range quality, ambil vendor terdekat
                    fallback = min(self.vendor_categories[cat], key=lambda x: abs(x["quality"] - quality))
                    cheapest_names.append(fallback["name"])
            return cheapest_names
    
        # Memulai loop yang mencoba menurunkan nilai kualitas mulai dari satu tingkat di bawah nilai asli hingga 1.
        for quality in range(original_quality - 1, 0, -1):
            cost = self.estimate_categories_cost(selected_categories, quality) # Menghitung estimasi total biaya untuk kategori yang dipilih dengan nilai kualitas baru
            if cost <= self.budget and cost > 0: # Jika biaya yang dihitung kurang dari atau sama dengan anggaran dan lebih dari 0, maka solusi yang layak telah ditemukan.
                
                # Memanggil fungsi pembantu get_cheapest_vendors untuk mendapatkan vendor termurah berdasarkan kategori dan kualitas baru.
                chosen_vendors = get_cheapest_vendors(selected_categories, quality)
                self.recommended_vendors = set(chosen_vendors) # Menyimpan vendor-vendor tersebut ke atribut 
                return {
                    "quality_change": True,
                    "new_quality": quality,
                    "removed_categories": [],
                    "new_categories": selected_categories,
                    "new_cost": cost
                }
        
        # Jika menurunkan kualitas tidak cukup, coba menghapus kategori berdasarkan prioritas
        sorted_categories = sorted(selected_categories, 
                                key=lambda cat: self.category_priorities.get(cat, 999))
        
        # Coba berbagai tingkat kualitas dengan lebih sedikit kategori
        for quality in range(original_quality, 0, -1): # Memulai loop dengan mencoba berbagai nilai kualitas mulai dari nilai asli hingga 1.
            for i in range(len(sorted_categories)): # ntuk setiap nilai kualitas, mencoba menghapus kategori dengan loop yang mengurangi satu kategori pada setiap iterasi.
                test_categories = sorted_categories[:-(i+1)] if i > 0 else sorted_categories
                cost = self.estimate_categories_cost(test_categories, quality) # Menghitung estimasi biaya untuk subset kategori tersebut dengan nilai kualitas saat ini.
                
                if cost <= self.budget and cost > 0: # Jika total biaya sesuai dengan anggaran (tidak melebihi dan lebih dari 0), maka simpan kategori yang dihapus.
                    removed = [cat for cat in original_categories if cat not in test_categories] # Membuat list removed yang berisi kategori yang tidak ada di test_categories dibandingkan dengan daftar kategori asli.
                    chosen_vendors = get_cheapest_vendors(test_categories, quality)
                    self.recommended_vendors = set(chosen_vendors) # Menyimpan vendor-vendor rekomendasi ke atribut 
                    return {
                        "quality_change": quality != original_quality,
                        "new_quality": quality,
                        "removed_categories": removed,
                        "new_categories": test_categories,
                        "new_cost": cost
                    }
        
        # Jika masih belum menemukan solusi, coba optimasi dengan hanya menggunakan satu kategori dengan prioritas tertinggi. 
        if sorted_categories:
            for i in range(len(sorted_categories)):
                highest_priority = [sorted_categories[i]]
                cost = self.estimate_categories_cost(highest_priority, 1)
                if cost <= self.budget and cost > 0:
                    removed = [cat for cat in original_categories if cat not in highest_priority]
                    chosen_vendors = get_cheapest_vendors(highest_priority, 1)
                    self.recommended_vendors = set(chosen_vendors)
                    return {
                        "quality_change": True,
                        "new_quality": 1,
                        "removed_categories": removed,
                        "new_categories": highest_priority,
                        "new_cost": cost
                    }
        
        # Jika semua optimasi gagal, tampilkan peringatan & hentikan proses pembayaran
        messagebox.showerror("Peringatan", "Tidak ada vendor yang sesuai dengan anggaran Anda. "
                                        "Silakan tambah anggaran atau pilih kategori lain.")
        return None  # Mencegah lanjut ke halaman pembayaran



    def show_budget_breakdown(self, categories, estimated_cost):
        """Show a message box with budget breakdown for selected categories"""
        breakdown_message = "Perkiraan Biaya per Kategori:\n\n"
        
        for category in categories:
            # Get vendors that match our quality range
            matching_vendors = [vendor for vendor in self.vendor_categories[category] 
                               if self.quality_range - 1 <= vendor["quality"] <= self.quality_range + 1]
            
            if matching_vendors:
                cheapest_vendor = min(matching_vendors, key=lambda x: x["price"])
                breakdown_message += f"{category}: Rp. {self.format_number(cheapest_vendor['price'])}\n"
            else:
                closest_vendor = min(self.vendor_categories[category], 
                                    key=lambda x: abs(x["quality"] - self.quality_range))
                breakdown_message += f"{category}: Rp. {self.format_number(closest_vendor['price'])}\n"
        
        breakdown_message += f"\nTotal Perkiraan: Rp. {self.format_number(estimated_cost)}"
        breakdown_message += f"\nBudget Anda: Rp. {self.format_number(self.budget)}"
        
        if estimated_cost > self.budget:
            kekurangan = estimated_cost - self.budget
            breakdown_message += f"\nKekurangan: Rp. {self.format_number(kekurangan)}"
        else:
            sisa = self.budget - estimated_cost
            breakdown_message += f"\nSisa Budget: Rp. {self.format_number(sisa)}"
        
        messagebox.showinfo("Perkiraan Biaya Kategori", breakdown_message)

    # Revisi Tambahan agar pengguna bisa memilih Vendor Manual
    def show_vendor_selection_frame(self):
        if self.current_frame:
            self.current_frame.destroy()
        
        frame = tk.Frame(self.root, bg="#FFF0F5")
        frame.pack(fill="both", expand=True)
        
        # Header
        header_frame = tk.Frame(frame, bg="#FF69B4")
        header_frame.pack(fill="x", pady=10)
        
        header_label = tk.Label(header_frame, text="Select Vendors", font=("Arial", 24, "bold"), 
                                bg="#FF69B4", fg="white", pady=10)
        header_label.pack()
        
        # Create a canvas with scrollbar for vendor selection
        canvas_frame = tk.Frame(frame, bg="#FFF0F5")
        canvas_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        canvas = tk.Canvas(canvas_frame, bg="#FFF0F5", highlightthickness=0)
        scrollbar = tk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
        
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Create a frame inside the canvas to hold all vendor options
        vendors_frame = tk.Frame(canvas, bg="#FFF0F5")
        canvas.create_window((0, 0), window=vendors_frame, anchor="nw")
        
        # Revisi info budget anggaran pengguna
        budget_label = tk.Label(vendors_frame, text=f"Budget: Rp. {self.format_number(self.budget)} • Quality Level: {self.quality_range}★", 
                                font=("Arial", 14, "bold"), bg="#FFF0F5", pady=10)
        budget_label.pack(anchor="w")

        self.vendor_options = {}
        row = 0

        # Pastikan self.recommended_vendors selalu ada
        if not hasattr(self, "recommended_vendors"):
            self.recommended_vendors = set()

        # For each selected category, show matching vendors
        for category in self.selected_categories:
            cat_frame = tk.LabelFrame(vendors_frame, text=category, font=("Arial", 14, "bold"), bg="#FFF0F5", padx=10, pady=10)
            cat_frame.pack(fill="x", expand=True, pady=10)
            
            # Filter vendors by quality
            vendors = [v for v in self.vendor_categories[category] 
                    if self.quality_range - 1 <= v["quality"] <= self.quality_range + 1]
            
            # If no vendors match the quality range, show the closest ones
            if not vendors:
                vendors = sorted(self.vendor_categories[category], 
                                key=lambda x: abs(x["quality"] - self.quality_range))[:4]
            
            # Create radio button group for each category
            var = tk.StringVar()
            self.vendor_options[category] = var
            
            for i, vendor in enumerate(vendors):
                quality_stars = "★" * vendor["quality"] + "☆" * (5 - vendor["quality"])
                
                vendor_text = f"{vendor['name']} - {quality_stars} - Rp. {self.format_number(vendor['price'])}"
                
                # Muncul Tanda Hijau Rekomendasi
                if vendor['name'] in self.recommended_vendors:
                    vendor_text += " ✅ (Rekomendasi yang telah disetujui)"
                    bg_color = "#E0FFE0"
                else:
                    bg_color = "#FFF0F5"
                
                rb = tk.Radiobutton(cat_frame, text=vendor_text, 
                                    variable=var, value=vendor['name'], font=("Arial", 12), 
                                    bg=bg_color, padx=10, pady=5)
                rb.grid(row=row, column=0, sticky="w", pady=2)
                row += 1
            
            # Set the default selection to the first vendor
            if vendors:
                var.set(vendors[0]['name'])
        
        # Buttons frame
        buttons_frame = tk.Frame(vendors_frame, bg="#FFF0F5")
        buttons_frame.pack(pady=20)
        
        next_button = tk.Button(buttons_frame, text="Selanjutnya", font=("Arial", 12), bg="#FF69B4", fg="white",
                                padx=20, pady=10, command=self.save_vendor_selection)
        next_button.pack(side="left", padx=10)
        
        back_button = tk.Button(buttons_frame, text="Kembali", font=("Arial", 12), bg="#888888", fg="white",
                                padx=20, pady=10, command=self.show_category_selection_frame)
        back_button.pack(side="left", padx=10)
        
        vendors_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))
        
        def _on_mousewheel(event):
            if canvas.winfo_exists():  # Cek kalau canvas masih ada
                canvas.yview_scroll(int(-1*(event.delta/120)), "units")

        
        # Footer
        footer_frame = tk.Frame(frame, bg="#FF69B4")
        footer_frame.pack(fill="x", side="bottom")
        
        footer_label = tk.Label(footer_frame, text="© 2025 Wedding Planner App", font=("Arial", 10), 
                                bg="#FF69B4", fg="white", pady=5)
        footer_label.pack()
        
        self.current_frame = frame

    def save_vendor_selection(self):
        # Get the selected vendors from each category
        self.selected_vendors = {}
        total_cost = 0
        
        for category in self.selected_categories:
            selected_vendor_name = self.vendor_options[category].get()
            
            # Find the vendor object that matches the selected name
            for vendor in self.vendor_categories[category]:
                if vendor["name"] == selected_vendor_name:
                    self.selected_vendors[category] = vendor
                    total_cost += vendor["price"]
                    break
        
        # Check if the total cost exceeds the budget
        if total_cost > self.budget:
            # Apply backtracking to optimize vendor selection
            optimized_result = self.optimize_selected_vendors()
            
            # Muncul Notifikasi Anggaran dan Rekomendasi
            if optimized_result:
                warning_message = ("Total biaya melebihi anggaran Anda.\n\n"
                                 "Kami telah menyarankan beberapa perubahan untuk menyesuaikan dengan budget Anda:")
                if optimized_result["new_cost"] == 0:
                    messagebox.showerror("Error", "Budget Anda terlalu kecil untuk membeli vendor apa pun.\nSilakan tambahkan budget atau pilih lebih sedikit kategori.")
                    return

                # Notifikasi Rekomendasi
                if optimized_result["quality_changes"]:
                    warning_message += "\n\n• Kualitas vendor yang diubah:"
                    for cat, orig_vendor, new_vendor in optimized_result["quality_changes"]:
                        warning_message += f"\n  - {cat}: {orig_vendor['name']} ({orig_vendor['quality']}★) → {new_vendor['name']} ({new_vendor['quality']}★)"
                
                if optimized_result["removed_categories"]:
                    warning_message += "\n\n• Kategori yang dihapus karena prioritas rendah:"
                    for cat in optimized_result["removed_categories"]:
                        warning_message += f"\n  - {cat}"
                
                warning_message += (f"\n\nTotal biaya awal: Rp. {self.format_number(total_cost)}"
                                  f"\nTotal biaya setelah optimasi: Rp. {self.format_number(optimized_result['new_cost'])}"
                                  f"\nBudget Anda: Rp. {self.format_number(self.budget)}")
                
                # Ask if user wants to accept these recommendations
                continue_with_optimization = messagebox.askyesno("Rekomendasi Optimasi Vendor", warning_message + "\n\nApakah Anda ingin melanjutkan dengan rekomendasi ini?")
                
                if continue_with_optimization:
                    # Apply the optimization
                    self.selected_categories = optimized_result["new_categories"]
                    self.selected_vendors = optimized_result["new_vendors"]
                    total_cost = optimized_result["new_cost"]
                    
                    # Show a message about the changes
                    messagebox.showinfo("Perubahan Diterapkan", 
                                      "Perubahan vendor telah diterapkan sesuai dengan rekomendasi.")
                    
                    # Continue to payment if budget is now sufficient
                    if total_cost <= self.budget:
                        self.show_payment_method_frame()
                    else:
                        # Still not enough budget
                        messagebox.showerror("Budget Tidak Cukup", 
                                           "Maaf, budget Anda masih tidak mencukupi bahkan setelah optimasi.")
                else:
                    # User rejected the optimization
                    insufficient_budget = messagebox.askyesno("Budget Tidak Cukup", 
                                                           f"Total biaya Rp. {self.format_number(total_cost)} melebihi budget Anda Rp. {self.format_number(self.budget)}.\n\nApakah Anda ingin mengubah pilihan vendor atau menambah budget?")
                    if insufficient_budget:
                        # Back to vendor selection
                        return
            else:
                # If optimization failed completely
                messagebox.showerror("Budget Tidak Cukup", 
                                   f"Maaf, budget Anda Rp. {self.format_number(self.budget)} tidak mencukupi bahkan setelah optimasi.\n\nAnda perlu menambah budget atau mengurangi kategori vendor.")
                return
        else:
            # Budget is sufficient, proceed to payment
            self.show_payment_method_frame()
    
    def optimize_selected_vendors(self):
        """Use backtracking to optimize vendor selection based on budget constraints"""
        original_cost = 0 # Menyimpan data vendor asli sebelum optimasi.
        original_vendors = self.selected_vendors.copy()
        original_categories = self.selected_categories.copy()
        
        # Calculate original cost
        for vendor in original_vendors.values():
            original_cost += vendor["price"] # Menghitung total biaya vendor yang dipilih pengguna.
        
        # Try replacing high-quality vendors with lower quality ones first
        new_vendors = original_vendors.copy()
        quality_changes = []
        
        # Sort categories by priority (lower number = higher priority)
        sorted_categories = sorted(original_categories, 
                                 key=lambda cat: self.category_priorities.get(cat, 999))
        
        # Reverse the order to try changing lower priority categories first
        for category in reversed(sorted_categories):
            current_vendor = new_vendors.get(category)
            if current_vendor:
                # Find all vendors with lower quality
                lower_quality_vendors = [v for v in self.vendor_categories[category] 
                                       if v["quality"] < current_vendor["quality"]]
                
                # Sort by quality (highest to lowest)
                lower_quality_vendors.sort(key=lambda x: -x["quality"])
                
                for vendor in lower_quality_vendors:
                    # Calculate new cost if we replace this vendor
                    new_cost = sum(v["price"] for v in new_vendors.values()) - current_vendor["price"] + vendor["price"]
                    
                    if new_cost <= self.budget:
                        # This change makes the budget sufficient
                        quality_changes.append((category, current_vendor, vendor))
                        new_vendors[category] = vendor
                        
                        return {
                            "quality_changes": quality_changes,
                            "removed_categories": [],
                            "new_categories": original_categories,
                            "new_vendors": new_vendors,
                            "new_cost": new_cost
                        }
                    else:
                        # Still not enough, make the change and continue
                        quality_changes.append((category, current_vendor, vendor))
                        new_vendors[category] = vendor
        
        # If changing quality isn't enough, try removing categories by priority
        removed_categories = []
        new_cost = sum(v["price"] for v in new_vendors.values())
        
        # If we're still over budget, try removing categories one by one, starting with lowest priority
        if new_cost > self.budget:
            for category in reversed(sorted_categories):
                if category in new_vendors:
                    # Calculate cost without this category
                    removed_vendor_price = new_vendors[category]["price"]
                    new_cost -= removed_vendor_price
                    
                    # Remove the category
                    removed_categories.append(category)
                    del new_vendors[category]
                    
                    if new_cost <= self.budget:
                        # We've reached a solution
                        new_categories = [c for c in original_categories if c not in removed_categories]
                        
                        return {
                            "quality_changes": quality_changes,
                            "removed_categories": removed_categories,
                            "new_categories": new_categories,
                            "new_vendors": new_vendors,
                            "new_cost": new_cost
                        }
        
        # If we still haven't found a solution, try just keeping the highest priority category
        # with the lowest quality vendor
        if sorted_categories:
            highest_priority = sorted_categories[0]
            lowest_quality_vendor = min(self.vendor_categories[highest_priority], key=lambda x: x["quality"])
            
            if lowest_quality_vendor["price"] <= self.budget:
                return {
                    "quality_changes": [(highest_priority, original_vendors.get(highest_priority, {}), lowest_quality_vendor)],
                    "removed_categories": [c for c in original_categories if c != highest_priority],
                    "new_categories": [highest_priority],
                    "new_vendors": {highest_priority: lowest_quality_vendor},
                    "new_cost": lowest_quality_vendor["price"]
                }
        
        # If all optimizations fail
        return None
    
    def show_payment_method_frame(self):
        if self.current_frame:
            self.current_frame.destroy()
        
        # Frame utama halaman Payment Method
        frame = tk.Frame(self.root, bg="#FFF0F5")
        frame.pack(fill="both", expand=True)
        
        # Header (di luar canvas, agar header tidak ikut scroll)
        header_frame = tk.Frame(frame, bg="#FF69B4")
        header_frame.pack(fill="x", pady=10)
        
        header_label = tk.Label(header_frame, text="Payment Method", font=("Arial", 24, "bold"), 
                                bg="#FF69B4", fg="white", pady=10)
        header_label.pack()
        
        # Canvas Frame (untuk membuat area yang bisa discroll)
        canvas_frame = tk.Frame(frame, bg="#FFF0F5")
        canvas_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Canvas & Scrollbar
        canvas = tk.Canvas(canvas_frame, bg="#FFF0F5", highlightthickness=0)
        scrollbar = tk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
        
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Frame tempat konten Payment Method (di dalam canvas)
        payment_frame = tk.Frame(canvas, bg="#FFF0F5")
        canvas.create_window((0, 0), window=payment_frame, anchor="nw")
        
        # Update scrollregion ketika payment_frame berubah ukuran
        payment_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        
        # ------------------ Mulai isi konten Payment Method di dalam payment_frame ------------------
        
        # Hitung total cost
        total_cost = sum(vendor["price"] for vendor in self.selected_vendors.values())
        
        # Judul Ringkasan Pesanan
        summary_label = tk.Label(payment_frame, text="Ringkasan Pesanan", font=("Arial", 16, "bold"), bg="#FFF0F5")
        summary_label.pack(pady=(0, 20))
        
        # Frame ringkasan pesanan (kotak putih dengan border)
        summary_frame = tk.Frame(payment_frame, bg="#FFF0F5", bd=2, relief="solid")
        summary_frame.pack(fill="x", padx=30, pady=10)
        
        # Tampilkan daftar vendor yang dipilih
        for category, vendor in self.selected_vendors.items():
            item_frame = tk.Frame(summary_frame, bg="#FFF0F5")
            item_frame.pack(fill="x", padx=10, pady=5)
            
            category_label = tk.Label(item_frame, text=category, font=("Arial", 12), bg="#FFF0F5", width=20, anchor="w")
            category_label.pack(side="left")
            
            vendor_label = tk.Label(item_frame, text=vendor["name"], font=("Arial", 12), bg="#FFF0F5", width=20, anchor="w")
            vendor_label.pack(side="left")
            
            price_label = tk.Label(item_frame, text=f"Rp. {self.format_number(vendor['price'])}", 
                                font=("Arial", 12), bg="#FFF0F5", width=15, anchor="e")
            price_label.pack(side="left")
        
        # Garis pemisah
        separator = tk.Frame(summary_frame, height=2, bg="#FF69B4")
        separator.pack(fill="x", padx=10, pady=5)
        
        # Bagian total
        total_frame = tk.Frame(summary_frame, bg="#FFF0F5")
        total_frame.pack(fill="x", padx=10, pady=5)
        
        total_label = tk.Label(total_frame, text="Total", font=("Arial", 14, "bold"), bg="#FFF0F5", width=20, anchor="w")
        total_label.pack(side="left")
        
        spacer = tk.Label(total_frame, text="", bg="#FFF0F5", width=20)
        spacer.pack(side="left")
        
        total_price = tk.Label(total_frame, text=f"Rp. {self.format_number(total_cost)}", 
                            font=("Arial", 14, "bold"), bg="#FFF0F5", width=15, anchor="e")
        total_price.pack(side="left")
        
        # Info budget
        budget_info = tk.Label(payment_frame, text=f"Budget Anda: Rp. {self.format_number(self.budget)}", 
                            font=("Arial", 12), bg="#FFF0F5")
        budget_info.pack(pady=10)
        
        # Metode pembayaran
        payment_label = tk.Label(payment_frame, text="Pilih Metode Pembayaran:", font=("Arial", 14, "bold"), 
                                bg="#FFF0F5", pady=10)
        payment_label.pack()
        
        # Opsi pembayaran
        self.payment_var = tk.StringVar(value="BCA")
        payment_options_frame = tk.Frame(payment_frame, bg="#FFF0F5")
        payment_options_frame.pack(pady=10)
        
        banks = ["BCA", "BRI", "MANDIRI"]
        
        for bank in banks:
            bank_frame = tk.Frame(payment_options_frame, bg="#FFF0F5", bd=2, relief="solid", padx=10, pady=10)
            bank_frame.pack(side="left", padx=10)
            
            rb = tk.Radiobutton(bank_frame, text=bank, variable=self.payment_var, value=bank, 
                                font=("Arial", 12, "bold"), bg="#FFF0F5", pady=5)
            rb.pack()
        
        # Tombol aksi
        buttons_frame = tk.Frame(payment_frame, bg="#FFF0F5")
        buttons_frame.pack(pady=20)
        
        pay_button = tk.Button(buttons_frame, text="Bayar Sekarang", font=("Arial", 12), bg="#FF69B4", fg="white",
                            padx=20, pady=10, command=self.process_payment)
        if total_cost <= self.budget:
            pay_button.configure(state="normal")
        else:
            pay_button.configure(state="disabled")
        pay_button.pack(side="left", padx=10)
        
        back_button = tk.Button(buttons_frame, text="Kembali", font=("Arial", 12), bg="#888888", fg="white",
                                padx=20, pady=10, command=self.show_vendor_selection_frame)
        back_button.pack(side="left", padx=10)
        
        # ------------------ Akhir konten Payment Method ------------------
        
        # Footer (di luar canvas, agar footer tidak ikut scroll)
        footer_frame = tk.Frame(frame, bg="#FF69B4")
        footer_frame.pack(fill="x", side="bottom")
        
        footer_label = tk.Label(footer_frame, text="© 2025 Wedding Planner App", font=("Arial", 10), 
                                bg="#FF69B4", fg="white", pady=5)
        footer_label.pack()
        
        self.current_frame = frame
    
    def process_payment(self):
        # Get selected payment method
        payment_method = self.payment_var.get()
        
        # Simulate payment processing
        processing_message = f"Memproses pembayaran melalui {payment_method}..."
        messagebox.showinfo("Memproses Pembayaran", processing_message)
        
        # Calculate total cost
        total_cost = sum(vendor["price"] for vendor in self.selected_vendors.values())
        
        if total_cost == 0:
            messagebox.showerror("Error", "Tidak ada vendor yang dipilih. Anda tidak dapat melanjutkan ke pembayaran.")
            return

        # Check if budget is sufficient
        if total_cost > self.budget:
            messagebox.showerror("Pembayaran Gagal", 
                               f"Maaf, total biaya Rp. {self.format_number(total_cost)} melebihi budget Anda Rp. {self.format_number(self.budget)}.")
            return
        
        # Show payment success
        success_message = f"Pembayaran berhasil menggunakan {payment_method}!\n\nTotal Pembayaran: Rp. {self.format_number(total_cost)}"
        messagebox.showinfo("Pembayaran Berhasil", success_message)
        
        # Proceed to confirmation screen
        self.show_confirmation_screen()
    
    def show_confirmation_screen(self):
        if self.current_frame:
            self.current_frame.destroy()

        frame = tk.Frame(self.root, bg="#FFF0F5")
        frame.pack(fill="both", expand=True)

        # Header
        header_frame = tk.Frame(frame, bg="#FF69B4")
        header_frame.pack(fill="x", pady=10)

        header_label = tk.Label(header_frame, text="Konfirmasi Pemesanan", font=("Arial", 24, "bold"), 
                                bg="#FF69B4", fg="white", pady=10)
        header_label.pack()

        # Canvas & Scrollbar untuk scroll halaman
        canvas_frame = tk.Frame(frame, bg="#FFF0F5")
        canvas_frame.pack(fill="both", expand=True, padx=20, pady=20)

        canvas = tk.Canvas(canvas_frame, bg="#FFF0F5", highlightthickness=0)
        scrollbar = tk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Frame untuk isi halaman (di dalam Canvas)
        content_frame = tk.Frame(canvas, bg="#FFF0F5")
        canvas.create_window((0, 0), window=content_frame, anchor="nw")

        # Bind agar scrollbar bisa bekerja dengan isi halaman
        content_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Success icon/text
        success_label = tk.Label(content_frame, text="✓", font=("Arial", 48), fg="#4CAF50", bg="#FFF0F5")
        success_label.pack()

        thank_you = tk.Label(content_frame, text="Terima Kasih!", font=("Arial", 20, "bold"), bg="#FFF0F5", pady=10)
        thank_you.pack()

        message = tk.Label(content_frame, text="Pesanan Anda telah berhasil diproses.", font=("Arial", 14), bg="#FFF0F5")
        message.pack()

        # Order details
        details_frame = tk.Frame(content_frame, bg="#FFF0F5", pady=20)
        details_frame.pack()

        order_label = tk.Label(details_frame, text="Detail Pesanan:", font=("Arial", 14, "bold"), bg="#FFF0F5", anchor="w")
        order_label.pack(anchor="w")

        # Display selected vendors
        for category, vendor in self.selected_vendors.items():
            item = tk.Label(details_frame, text=f"• {category}: {vendor['name']} - Rp. {self.format_number(vendor['price'])}", 
                            font=("Arial", 12), bg="#FFF0F5", anchor="w")
            item.pack(anchor="w", pady=2)

        # Calculate total cost
        total_cost = sum(vendor["price"] for vendor in self.selected_vendors.values())

        # Total
        total = tk.Label(details_frame, text=f"Total: Rp. {self.format_number(total_cost)}", 
                        font=("Arial", 14, "bold"), bg="#FFF0F5", pady=10)
        total.pack(anchor="w")

        # Payment method
        payment = tk.Label(details_frame, text=f"Metode Pembayaran: {self.payment_var.get()}", 
                        font=("Arial", 12), bg="#FFF0F5")
        payment.pack(anchor="w")

        # Revisi Tombol Kembali Ke Halaman Utama
        home_button = tk.Button(content_frame, text="Kembali ke Halaman Utama", font=("Arial", 14), bg="#FF69B4", fg="white",
                                padx=20, pady=10, command=self.reset_and_return_home)
        home_button.pack(pady=30)

        # Footer
        footer_frame = tk.Frame(frame, bg="#FF69B4")
        footer_frame.pack(fill="x", side="bottom")

        footer_label = tk.Label(footer_frame, text="© 2025 Wedding Planner App", font=("Arial", 10), 
                                bg="#FF69B4", fg="white", pady=5)
        footer_label.pack()

        self.current_frame = frame

        # Tambahan agar teks center dan tombol mudah terlihat:
        success_label.pack_configure(anchor="center")
        thank_you.pack_configure(anchor="center")
        message.pack_configure(anchor="center")
        order_label.pack_configure(anchor="center")
        total.pack_configure(anchor="center")
        payment.pack_configure(anchor="center")
        home_button.pack_configure(anchor="center")

        # Bagi setiap label vendor di details_frame, center-kan juga
        for w in details_frame.winfo_children():
            w.pack_configure(anchor="center")

    def reset_and_return_home(self):
        # Reset all app state variables
        self.budget = 0
        self.quality_range = 0
        self.selected_categories = []
        self.selected_vendors = {}
        self.payment_method = ""
        
        # Return to welcome screen
        self.show_welcome_frame()

    
    def format_number(self, number):
        """Format number with thousands separators"""
        return locale.format_string('%d', number, grouping=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = WeddingPlannerApp(root)
    root.mainloop()
