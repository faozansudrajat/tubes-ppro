import mahasiswa as mhs
import topic as tpc
import grade as gr
import submission as sbm


def login(dict_mhs):
    global NIM_LOGIN
    global ADMIN_LOGIN
    print('1: Login Mahasiswa')
    print('2: Login Admin')
    print('0: Exit')
    pilih = int(input('Masukkan pilihan anda (1/2): '))
    if pilih == 1:
        NIM_LOGIN = mhs.login_mhs(dict_mhs)
    elif pilih == 2:
        ADMIN_LOGIN = True
    elif pilih == 0:
        print('Terima kasih!')
        exit()
        
                  


if __name__ == "__main__":
    #variable LAST_ID_ACTIVITY menentukan id_activity selanjutnya jika ada penambahan activity
    LAST_ID_ACTIVITY = 2
    NIM_LOGIN = ''
    ADMIN_LOGIN = False


    #key pada dict_mhs['data'] adalah NIM
    dict_mhs = {'field' : [('Nama', "^([a-zA-Z]+([ '-]| ')?[a-zA-Z]+){1,4}$"),
                           ('Email', '^([a-z0-9]+[._]?[a-z0-9]+)+[@]\w+[.]\w{2,3}'),
                           ('Password', '^[a-zA-Z0-9]{8,12}$')],
             'data' : {'113': {'Nama': 'Dummy', 'Email': 'dummy@telU.com', 'Password': '12345678'},
                       '114': {'Nama': 'Joni', 'Email': 'joni@telU.com', 'Password': '12345678'},
                       '115': {'Nama': 'jeje', 'Email': 'jeje@telU.com', 'Password': '12345678'}

                       }           
            }

    #Value pada key 'Activities' berupa list berisi id_activity
    list_topic = [{'Title': 'Dummy Topic 1', 'Description': 'Ini deskripsi topic 1', 'Activities':[0, 1]},
                    {'Title': 'Dummy Topic 2', 'Description': 'Ini deskripsi topic 2', 'Activities':[2]}
                  ]

    # key pada dict_activity adalah id_activity 
    dict_activity = {0: {'Title': 'Dummy Assignment 1', 'Type': 'assignment', 'Description': 'buatlah program Game'},
                         1: {'Title': 'Dummy material', 'Type': 'material', 'Description': 'slide minggu ini'},
                         2: {'Title': 'Dummy Assignment 2', 'Type': 'assignment', 'Description': 'buatlah program LMS'}
                         }

    # key pada dict_submission adalah id_activity 
    dict_submission = {0: {'113' : 'Ini jawaban mahasiswa 113',
                           '114': 'Ini jawaban mahasiswa 114'},
                        2: {'113' : 'Ini jawaban mahasiswa 113',
                           '114': 'Ini jawaban mahasiswa 114'}
                       }

    # key pada dict_grade adalah id_activity 
    dict_grade = {0: {'113' : 100}
                        
                  }


    while not NIM_LOGIN and not ADMIN_LOGIN:
        login(dict_mhs)
        if NIM_LOGIN:
            while True:
                print('1: Tampilkan topik dan aktifitas')
                print('2: Tampilkan semua submission')
                print('3: Tampilkan assignment belum disubmit')
                print('4: Submit assignment')
                print('5: Update submission')
                print('6: Delete submission')
                print('0: Logout')
                pilih = int(input('Pilihan anda: '))
                if pilih == 1:
                    tpc.show_topic(list_topic, dict_activity)
                elif pilih == 2:
                    sbm.show_my_submission(dict_submission, NIM_LOGIN)
                elif pilih == 3:
                    sbm.show_assignment_not_submit(dict_activity, dict_submission, NIM_LOGIN)
                if pilih == 4:
                    sbm.submit_assignment(dict_submission, list_topic, dict_activity, NIM_LOGIN)
                elif pilih == 5:
                    sbm.update_submission(dict_submission, list_topic, dict_activity, NIM_LOGIN)
                elif pilih == 6:
                    sbm.delete_submission(dict_submission, list_topic, dict_activity, NIM_LOGIN)
                elif pilih == 0:
                    NIM_LOGIN = ''
                    break
            
        elif ADMIN_LOGIN:
            while True:
                print('1: Menu terkait mahasiswa')
                print('2: Menu terkait topik dan aktifitas')
                print('3: Menu terkait submission')
                print('4: Menu terkait penilaian')
                print('0: Logout')
                pilih = int(input('Masukkan ID Menu: '))
                if pilih == 1:
                    while True:
                        print('Menu terkait mahasiswa:')
                        print('-----------------------')
                        print('1: Tampilkan data mahasiswa')
                        print('2: Tambah satu mahasiswa')
                        print('3: Tambah beberapa mahasiswa')
                        print('4: Update mahasiswa')
                        print('5: Hapus mahasiswa')
                        print('6: Print data mahasiswa ke file')
                        print('0: Kembali ke menu utama')
                        pilih2 = int(input('Masukkan ID Menu: '))
                        if pilih2 == 1:
                            mhs.show_data(dict_mhs)
                        elif pilih2 == 2:
                            mhs.add_one_mhs(dict_mhs)
                        elif pilih2 == 3:
                            mhs.add_many_mhs(dict_mhs)
                        elif pilih2 == 4:
                            mhs.update_mhs(dict_mhs)
                        elif pilih2 == 5:
                            mhs.delete_mhs(dict_mhs)
                        elif pilih2 == 6:
                            mhs.print_to_file(dict_mhs)
                        elif pilih2 == 0:
                            break
                elif pilih == 2:
                    while True:
                        print('Menu terkait topik dan aktifitas')
                        print('--------------------------------')
                        print('1: Tampilkan data topik dan aktifitas')
                        print('2: Tambah topik')
                        print('3: Update topik')
                        print('4: Hapus topik')
                        print('5: Tambah aktifitas')
                        print('6: Update aktifitas')
                        print('7: Hapus aktifitas')
                        print('8: Print data topik dan aktifitas ke file')
                        print('0: Kembali ke menu utama')
                        pilih2 = int(input('Masukkan ID Menu: '))
                        if pilih2 == 1:
                            tpc.show_topic(list_topic, dict_activity)
                        elif pilih2 == 2:
                            LAST_ID_ACTIVITY = tpc.add_topic(list_topic, dict_activity, LAST_ID_ACTIVITY)
                        elif pilih2 == 3:
                            tpc.update_topic(list_topic)
                        elif pilih2 == 4:
                            tpc.delete_topic(list_topic, dict_activity, dict_submission, dict_grade)
                        elif pilih2 == 5:
                            LAST_ID_ACTIVITY = tpc.add_activity(list_topic, dict_activity, LAST_ID_ACTIVITY)
                        elif pilih2 == 6:
                            tpc.udpate_activity(list_topic, dict_activity)
                        elif pilih2 == 7:
                            tpc.delete_activity(list_topic, dict_activity, dict_submission, dict_grade)
                        elif pilih2 == 8:
                            tpc.print_topic_to_file(list_topic, dict_activity)
                        elif pilih2 == 0:
                            break
                elif pilih == 3:
                    while True:
                        print('Menu terkait submission')
                        print('1: Tampilkan nim yang ada assignment belum submit')
                        print('2: Print data submission ke file')
                        print('0: Kembali ke menu utama')
                        pilih2 = int(input('Masukkan ID Menu: '))
                        if pilih2 == 1:
                            sbm.show_nim_not_submit(dict_mhs, dict_submission, dict_activity)
                        elif pilih2 == 2:
                            sbm.print_submissions_to_file(dict_submission, dict_activity)
                        elif pilih2 == 0:
                            break
                elif pilih == 4:
                    while True:
                        print('Menu terkait penilaian')
                        print('----------------------')
                        print('1: Tampilkan semua data nilai')
                        print('2: Tampilkan mahasiswa yang belum lengkap dinilai')
                        print('3: Beri nilai berdasarkan mahasiswa')
                        print('4: Tampilkan assignment yang belum lengkap dinilai')
                        print('5: Beri nilai berdasarkan assignment')
                        print('6: Tampilkan rekapan nilai assignment')
                        print('7: Tampilkan rekapan nilai mahasiswa')
                        print('8: Print data nilai ke file')
                        print('0: Kembali ke menu utama')
                        pilih2 = int(input('Masukkan ID Menu: '))
                        if pilih2 == 1:
                            gr.show_all_grade(dict_grade, dict_activity)
                        elif pilih2 == 2:
                            gr.show_mhs_not_graded(dict_submission, dict_grade)
                        elif pilih2 == 3:
                            gr.add_grade_by_mhs(dict_submission, dict_activity, dict_grade)
                        elif pilih2 == 4:
                            gr.show_assignment_not_graded(dict_submission, dict_activity, dict_grade)
                        elif pilih2 == 5:
                            gr.add_grade_by_assignment(dict_submission, dict_grade)
                        elif pilih2 == 6:
                            gr.report_by_assignment(dict_submission, dict_activity, dict_grade)
                        elif pilih2 == 7:
                            gr.report_by_mhs(dict_submission, dict_grade)
                        elif pilih2 == 8:
                            gr.print_grade_to_file(dict_grade, dict_activity)
                        elif pilih2 == 0:
                            break
                elif pilih == 0:
                    ADMIN_LOGIN = False
                    break