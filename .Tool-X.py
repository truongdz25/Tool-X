# Tên công cụ: - Bộ công cụ
# Tác giả: - truong Dz
# Ngày: - 17/08/2019
# Được cung cấp bởi: - Phần mềm của Aex

nhập khẩu hệ thống
nhập khẩu os
từ modules.logo nhập  cảnh
từ modules.menu nhập khẩu ToolX

lớp  chk ( đối tượng ):
  def  Chos ( tự ):
    nếu  " linux "  trong sys.pl platform:
      # Chạy Tool-X trên linux ....
      vượt qua
    elif  " darwin "  trong sys.pl platform:
      vượt qua
      # print ("Xin lỗi, hiện tại nó không có sẵn cho mac ...")
      ví dụ cũ
    elif  " giành chiến thắng "  trong sys.pl platform:
      in ( " Xin lỗi, hiện tại nó không có sẵn cho windows ... " )
      ví dụ cũ
    khác :
      print ( " Nếu Tool-X không hỗ trợ cho \ ' % s \' ngay bây giờ !!! "  % sys.pl platform)

def  Tool_X ():
  thử :
	chk (). chos ()
	ToolX ()

  ngoại trừ  KeyboardInterrupt :
	thoát ()
Công cụ_X ()

