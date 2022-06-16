import matplotlib.pyplot
from matplotlib import colors

if __name__ == '__main__':
# Gráfico padrão
# dias = [22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
# mortes = [45, 0, 18, 12, 18, 0, 0, 28, 10, 22]
#
# matplotlib.pyplot.plot(dias, mortes)
# matplotlib.pyplot.title('Número de mortes Covid 19')
# matplotlib.pyplot.xlabel('Dias')
# matplotlib.pyplot.ylabel('Mortes')
#
# matplotlib.pyplot.show()

# valid_values = [True, False]
# providers = [1, 2, 3]
# SLA
# fig, ax = matplotlib.pyplot.subplots()
# rects1 = ax.bar("Never Follow", 166, facecolor='#DBDBDB')
# rects2 = ax.bar("Follow User", 70, facecolor='#A7A7A7')
# rects3 = ax.bar("Faticanti et al.", 58, facecolor='#6C6C6C')
# rects4 = ax.bar("Argos", 50, facecolor='#393939')
#
# ax.set_ylabel('SLA')
# ax.set_xlabel('Algorithm')
#
# ax.bar_label(rects1, padding=3)
# ax.bar_label(rects2, padding=3)
# ax.bar_label(rects3, padding=3)
# ax.bar_label(rects4, padding=3)
#
# fig.tight_layout()
#
# matplotlib.pyplot.show()
# matplotlib.pyplot.bar("Never Migrate", 166, facecolor = '#DBDBDB')
# matplotlib.pyplot.bar("Follow User", 70, facecolor = '#A7A7A7')
# matplotlib.pyplot.bar("Faticanti et al.", 58, facecolor = '#6C6C6C')
# matplotlib.pyplot.bar("Argos", 50, facecolor = '#393939')
#
# matplotlib.pyplot.xlabel('Algorithm')
# matplotlib.pyplot.ylabel('SLA Violations')
# matplotlib.pyplot.show()

# Migrations
# matplotlib.pyplot.bar("Never Migrate", 0, facecolor='#DBDBDB')
# matplotlib.pyplot.bar("Follow User", 4535, facecolor='#A7A7A7')
# matplotlib.pyplot.bar("Faticanti et al.", 62, facecolor='#6C6C6C')
# matplotlib.pyplot.bar("Argos", 90, facecolor='#393939')
#
# matplotlib.pyplot.xlabel('Algorithm')
# matplotlib.pyplot.ylabel('Migrations')
# matplotlib.pyplot.show()

# Privacy Violations
# algorithms = ['Never Migrate', 'Follow User', 'Fatincanti et al.', 'Argos']
# privacyViolations = [2170, 2109, 1931, 1674]

# never = matplotlib.pyplot.bar("Never Migrate", 2170, facecolor='#DBDBDB')
# follow = matplotlib.pyplot.bar("Follow User", 2109, facecolor='#A7A7A7')
# faticanti = matplotlib.pyplot.bar("Faticanti et al.", 1931, facecolor='#6C6C6C')
# argos = matplotlib.pyplot.bar("Argos", 1674, facecolor='#393939')

# matplotlib.pyplot.bar("Never Migrate", 2170, facecolor='#DBDBDB', bottom=1)
# matplotlib.pyplot.bar("Follow User", 2109, facecolor='#A7A7A7')
# matplotlib.pyplot.bar("Faticanti et al.", 1931, facecolor='#6C6C6C')
# matplotlib.pyplot.bar("Argos", 1674, facecolor='#393939')

# fig, ax = matplotlib.pyplot.subplots()
# rects1 = ax.bar("Never Migrate", 2170, facecolor='#DBDBDB')
# rects2 = ax.bar("Follow User", 2109, facecolor='#A7A7A7')
#
# ax.set_xlabel('Migrations')
# ax.set_ylabel('Algorithm')
#
#
# ax.bar_label(rects1, padding=3)
# ax.bar_label(rects2, padding=3)
#
# fig.tight_layout()
#
# matplotlib.pyplot.show()


# valid_values = [True, False]
# providers = [1, 2, 3]
# Migrations
# fig, ax = matplotlib.pyplot.subplots()
# rects1 = ax.bar("Never Follow", 0, facecolor='#DBDBDB')
# rects2 = ax.bar("Follow User", 4535, facecolor='#A7A7A7')
# rects3 = ax.bar("Faticanti et al.", 62, facecolor='#6C6C6C')
# rects4 = ax.bar("Argos", 90, facecolor='#393939')
#
# ax.set_ylabel('Migrations')
# ax.set_xlabel('Algorithm')
#
# ax.bar_label(rects1, padding=3)
# ax.bar_label(rects2, padding=3)
# ax.bar_label(rects3, padding=3)
# ax.bar_label(rects4, padding=3)
#
# fig.tight_layout()
#
# matplotlib.pyplot.show()

# valid_values = [True, False]
# providers = [1, 2, 3]
# Privacy Violations
# fig, ax = matplotlib.pyplot.subplots()
# rects1 = ax.bar("Never Follow", 2170, facecolor='#DBDBDB')
# rects2 = ax.bar("Follow User", 2109, facecolor='#A7A7A7')
# rects3 = ax.bar("Faticanti et al.", 1931, facecolor='#6C6C6C')
# rects4 = ax.bar("Argos", 1674, facecolor='#393939')
#
# ax.set_ylabel('Privacy Violations')
# ax.set_xlabel('Algorithm')
#
# ax.bar_label(rects1, padding=3)
# ax.bar_label(rects2, padding=3)
# ax.bar_label(rects3, padding=3)
# ax.bar_label(rects4, padding=3)
#
# fig.tight_layout()
#
# matplotlib.pyplot.show()

# valid_values = [True, False]
# providers = [1, 2, 3, 4]
#     SLA

    # fig, ax = matplotlib.pyplot.subplots()
    # rects1 = ax.bar("Never Follow", 166, facecolor='#DBDBDB')
    # rects2 = ax.bar("Follow User", 70, facecolor='#A7A7A7')
    # rects3 = ax.bar("Faticanti et al.", 57, facecolor='#6C6C6C')
    # rects4 = ax.bar("Argos", 44, facecolor='#393939')
    #
    # ax.set_ylabel('SLA')
    # ax.set_xlabel('Algorithm')
    #
    # ax.bar_label(rects1, padding=3)
    # ax.bar_label(rects2, padding=3)
    # ax.bar_label(rects3, padding=3)
    # ax.bar_label(rects4, padding=3)
    #
    # fig.tight_layout()
    #
    # matplotlib.pyplot.show()


# valid_values = [True, False]
# providers = [1, 2, 3, 4]
#     Migrations

    # fig, ax = matplotlib.pyplot.subplots()
    # rects1 = ax.bar("Never Follow", 0, facecolor='#DBDBDB')
    # rects2 = ax.bar("Follow User", 4535, facecolor='#A7A7A7')
    # rects3 = ax.bar("Faticanti et al.", 63, facecolor='#6C6C6C')
    # rects4 = ax.bar("Argos", 84, facecolor='#393939')
    #
    # ax.set_ylabel('Migrations')
    # ax.set_xlabel('Algorithm')
    #
    # ax.bar_label(rects1, padding=3)
    # ax.bar_label(rects2, padding=3)
    # ax.bar_label(rects3, padding=3)
    # ax.bar_label(rects4, padding=3)
    #
    # fig.tight_layout()
    #
    # matplotlib.pyplot.show()


# valid_values = [True, False]
# providers = [1, 2, 3, 4]
#     Privacy Violations

    fig, ax = matplotlib.pyplot.subplots()
    rects1 = ax.bar("Never Follow", 2325, facecolor='#DBDBDB')
    rects2 = ax.bar("Follow User", 2321, facecolor='#A7A7A7')
    rects3 = ax.bar("Faticanti et al.", 2026, facecolor='#6C6C6C')
    rects4 = ax.bar("Argos", 1858, facecolor='#393939')

    ax.set_ylabel('Privacy Violations')
    ax.set_xlabel('Algorithm')

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)
    ax.bar_label(rects3, padding=3)
    ax.bar_label(rects4, padding=3)

    fig.tight_layout()

    matplotlib.pyplot.show()