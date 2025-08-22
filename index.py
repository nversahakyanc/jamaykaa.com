import os
import re
import concurrent.futures

# ✅ Your updated full menu HTML
NEW_MENU = """                <div class="offscreen-navigation">
                    <nav class="menu-main-by-mago-container">
                        <ul id="menu-main-by-mago-4" class="menu">
                            <li
                                class="menu-item menu-item-type-custom menu-item-object-custom current-menu-item current_page_item menu-item-home menu-item-4247">
                                <a href="/" aria-current="page">الرئيسيه</a>
                            </li>
                            <li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4248"><a
                                    href="#our-services">خدماتنا</a></li>
                            <li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4261"><a
                                    href="#who-we-are">معلومات عنّا</a></li>
                            <li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-5839"><a
                                    href="blog/">المدونة</a></li>
                            <li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4266"><a
                                    href="#achievements">إنجازتنا</a></li>
                            <li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4262"><a
                                    href="#client_testmonial">آراء العملاء</a></li>
                            <li
                                class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-5140">
                                <a href="#">تسجيل دخول​</a>
                                <ul class="sub-menu">
                                    <li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-5498">
                                        <a href="https://bit.ly/3WrMPvy">مسوق بالعمولة</a>
                                    </li>
                                    <li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-5499">
                                        <a href="https://bit.ly/3ULn3RH">تاجر</a>
                                    </li>
                                </ul>
                            </li>
                            <li id="menu-item-4267"
                                class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4266">
                                <a href="../utility-bill.html">فاتورة خدمات</a>
                            </li>
                            <li id="menu-item-4267"
                                class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4266">
                                <a href="../business-utility-bill.html"> فاتورة المرافق التجارية</a>
                            </li>
                            <li id="menu-item-4267"
                                class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4266">
                                <a href="../business-registration-certificate.html">شهادة تسجيل تجاري </a>
                            </li>
                            <li id="menu-item-4267"
                                class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4266">
                                <a href="../travel-visa.html">تأشيرة سفر</a>
                            </li>
                            <li id="menu-item-4267"
                                class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4266">
                                <a href="../car-title.html"> سند ملكية السيارة</a>
                            </li>
                            <li id="menu-item-4267"
                                class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4266">
                                <a href="../car-insurance.html">تأمين السيارة</a>
                            </li>
                            <li id="menu-item-4267"
                                class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4266">
                                <a href="../diploma.html">دبلوم </a>
                            </li>
                            <li id="menu-item-4267"
                                class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4266">
                                <a href="../ssn.html">رقم الضمان الاجتماعي</a>
                            </li>
                            <li id="menu-item-4267"
                                class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4266">
                                <a href="../passport.html">التعريف </a>
                            </li>
                            <li id="menu-item-4267"
                                class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4266">
                                <a href="../passport-photolook.html">جواز سفر فوتو لوك</a>
                            </li>
                            <li id="menu-item-4267"
                                class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4266">
                                <a href="../passport-other-pages.html">صفحات جواز السفر الأخرى</a>
                            </li>
                            <li id="menu-item-4267"
                                class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4266">
                                <a href="../driving-license.html">رخصة القيادة </a>
                            </li>
                            <li id="menu-item-4267"
                                class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4266">
                                <a href="../driving-license-photolook.html">رخصة قيادة </a>
                            </li>
                            <li id="menu-item-4267"
                                class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4266">
                                <a href="../id-card.html"> بطاقة هوية </a>
                            </li>
                            <li id="menu-item-4267"
                                class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4266">
                                <a href="../id-card-photolook.html"> صورة بطاقة الهوية الرسمية </a>
                            </li>
                            <li id="menu-item-4267"
                                class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4266">
                                <a href="../formal-id.html"> صورة الهوية الرسمية </a>
                            </li>
                            <li id="menu-item-4267"
                                class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4266">
                                <a href="../residence-permit.html"> تصريح الإقامة </a>
                            </li>
                            <li id="menu-item-4267"
                                class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4266">
                                <a href="../residence-permit-photolook.html"> صورة تصريح الإقامة </a>
                            </li>
                            <li id="menu-item-4267"
                                class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4266">
                                <a href="../student-ID.html"> بطاقة هوية الطالب </a>
                            </li>
                            <li id="menu-item-4267"
                                class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4266">
                                <a href="../health-insurance-card.html"> بطاقة التأمين الصحي </a>
                            </li>
                            <li id="menu-item-4267"
                                class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4266">
                                <a href="../tax-bill.html"> فاتورة الضرائب </a>
                            </li>
                            <li id="menu-item-4267"
                                class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4266">
                                <a href="../product-certificate.html"> شهادة المنتج </a>
                            </li>
                            <li id="menu-item-4267"
                                class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4266">
                                <a href="../arrival-card.html"> بطاقة الوصول </a>
                            </li>
                            <li id="menu-item-4267"
                                class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4266">
                                <a href="../mix.html"> خليط / مزيج </a>
                            </li>
                            <li id="menu-item-4267"
                                class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4266">
                                <a href="../mix-photolook.html"> ميكس صورة الهوية </a>
                            </li>
                            <li id="menu-item-4267"
                                class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4266">
                                <a href="../transcript.html"> كشف الدرجات </a>
                            </li>
                            <li id="menu-item-4267"
                                class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4266">
                                <a href="../paystub.html"> إيصال الراتب </a>
                            </li>
                            <li id="menu-item-4267"
                                class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4266">
                                <a href="../receipt.html"> إيصال دفع </a>
                            </li>
                            <li id="menu-item-4267"
                                class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4266">
                                <a href="../invoice.html"> فاتورة </a>
                            </li>
                            <li id="menu-item-4267"
                                class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4266">
                                <a href="../reference.html"> مرجع </a>
                            </li>
                            <li id="menu-item-4267"
                                class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4266">
                                <a href="../certificate.html"> شهادة </a>
                            </li>
                            <li id="menu-item-4267"
                                class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4266">
                                <a href="../bank-statement.html"> كشف حساب بنكي </a>
                            </li>
                            <li id="menu-item-4267"
                                class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4266">
                                <a href="../business-bank-statement.html"> كشف حساب بنكي تجاري </a>
                            </li>
                            <li id="menu-item-4267"
                                class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4266">
                                <a href="../booking.html">حجز </a>
                            </li>
                            <li id="menu-item-4267"
                                class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4266">
                                <a href="../credit-card.html">بطاقة ائتمان </a>
                            </li>
                            <li id="menu-item-4267"
                                class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4266">
                                <a href="../credit-card-photolook.html">مظهر فوتوغرافي لبطاقة ائتمان  </a>
                            </li>
                        </ul>
                    </nav>
                </div>"""

MENU_PATTERN = re.compile(
    r'<div class="offscreen-navigation.*?</div>',
    re.DOTALL | re.IGNORECASE
)

def replace_menu_in_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        new_content, count = MENU_PATTERN.subn(NEW_MENU, content)

        if count > 0 and new_content != content:  # only write if changed
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            return f"✅ Updated {filepath}"
        return f"⚠ No menu found in {filepath}"
    except Exception as e:
        return f"❌ Error {filepath}: {e}"

def update_all_html(root_folder, workers=8):
    files = []
    for root, dirs, filenames in os.walk(root_folder):
        for file in filenames:
            if file.endswith(".html"):
                files.append(os.path.join(root, file))

    print(f"Found {len(files)} HTML files")

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        for result in executor.map(replace_menu_in_file, files):
            print(result)

if __name__ == "__main__":
    project_root = "./product-certificate"
    update_all_html(project_root, workers=8)  # adjust workers to CPU cores
