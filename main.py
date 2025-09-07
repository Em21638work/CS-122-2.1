def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc, f_perc, nb_perc for your results
    ##################################################
    """
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    # my code
    mstudents = int(input("number of male students:"))
    fstudents = int(input("number of female students:"))
    nbstudents = int(input("number of non-binary students:"))
    total_students = mstudents + fstudents + nbstudents
    m_perc = (mstudents / total_students) * 100
    f_perc = (fstudents / total_students) * 100
    nb_perc = (nbstudents / total_students) * 100
    # end of my code
    print (f'The total number of students: {total_students}')
    print (f'The number of males, females, and non-binary: \t {mstudents} \t {fstudents} \t {nbstudents}')
    print(
        f'The percentage of males, females and non-binary \t {m_perc: .2f} \t {f_perc: .2f} \t {nb_perc: .2f}')
    return m_perc, f_perc, nb_perc


if __name__ == '__main__':
    main()
