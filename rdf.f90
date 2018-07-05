program rdf

implicit none
character :: a
integer :: nframes, natoms, nwater, nsodium, nclor, ii, jj, iP, NHist, k, ll
real :: L, dr, r, current_r, next_r, vol, rho, V, L2
real, parameter :: pi=3.1415926
real, dimension(:,:), allocatable :: na, cl
real, dimension(3) :: dr_vec
real, dimension(:), allocatable :: HistProfile

!-----------------------------------------------------------------------------------------------!
!					Reading the files					!
!-----------------------------------------------------------------------------------------------!
open(unit=20,file='param.txt',form='formatted',status='old')
open(unit=22,file='pos_na.txt',form='formatted',status='old')
open(unit=23,file='pos_cl.txt',form='formatted',status='old')

read(20,'(i5)') nframes
read(20,'(i5)') natoms
read(20,'(i5)') nwater
read(20,'(i5)') nsodium
read(20,'(i5)') nclor

!nframes = 1
!-----------------------------------------------------------------------------------------------!
!				Extracting the HistProfile information				!
!-----------------------------------------------------------------------------------------------!

! Important parameters for the HistProfile !
L = 30.3942
dr = 0.1
NHist = int(L/(2*dr))
L2 = L/2

allocate(Histprofile(NHist))
allocate(na(nsodium,3))
allocate(cl(nclor,3))
print *, nframes
read(22,*)
read(23,*)

HistProfile = 0.

do k = 1, nframes
   do ll =1,nsodium
       read(22,*) na(ll,1), na(ll,2), na(ll,3)
       read(23,*) cl(ll,1), cl(ll,2), cl(ll,3)
   end do
   do ii = 1, nsodium
      do jj = 1, nclor
	 dr_vec(1) = na(ii,1) - cl(jj,1)
	 dr_vec(2) = na(ii,2) - cl(jj,2)
	 dr_vec(3) = na(ii,3) - cl(jj,3)
	      
	 dr_vec(1) = dr_vec(1)-L*int(dr_vec(1)/L)
	 dr_vec(2) = dr_vec(2)-L*int(dr_vec(2)/L)
	 dr_vec(3) = dr_vec(3)-L*int(dr_vec(3)/L)

	 r=sqrt(dr_vec(1)*dr_vec(1)+dr_vec(2)*dr_vec(2)+dr_vec(3)*dr_vec(3))
         print *, r
	 if (r .lt. L2) then
            iP = int(r/dr)
	    HistProfile(iP) = HistProfile(iP)+1
	 end if
       end do
    end do
end do
!-----------------------------------------------------------------------------------------------!
!				Creating the g(r) function					!
!-----------------------------------------------------------------------------------------------!
V = L**3
rho = nsodium/V

open(unit=30,file='gr.dat',form='formatted',status='unknown')
do iP = 1, NHist
   !current_r = (iP-1)*dr + dr/2
   !next_r = current_r + dr
   !vol = (4.0d0/3.0d0)*pi*((next_r**3)-(current_r**3))
   vol = (4.0d0/3.0d0)*pi*((((iP+1)**3)-(iP**3))*dr**3)*rho
   HistProfile(iP) = HistProfile(iP)/(vol*nsodium*nframes)
   print *, HistProfile(iP)
   write(30,*) (iP+0.5)*dr, HistProfile(iP)
end do

close(20)
close(22)
close(23)
close(30)

end program
