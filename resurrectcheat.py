import services
import sims4.commands
import sims4.tuning.tunable
import tag
import traits.traits
from protocolbuffers import SimObjectAttributes_pb2 as protocols
from objects import ALL_HIDDEN_REASONS
import sims4.reload
from interactions.utils.death import DeathTracker

@sims4.commands.Command('resurrect', command_type=sims4.commands.CommandType.Live)
def get_resurrect_data(first_name='', last_name='', _connection=None):	
	info = services.sim_info_manager().get_sim_info_by_name(first_name, last_name)	
	output = sims4.commands.CheatOutput(_connection)	
	if info is not None:		
		output('Start')		
		output('1')
		info.trait_tracker.remove_traits_of_type(traits.traits.TraitType.GHOST)
		output('2')
		info.death_tracker.clear_death_type()
		output('3')
		info.update_age_callbacks()
		sim = info.get_sim_instance()
		if sim is not None:			
			output('4')
			sim.routing_context.ghost_route = False
			output('5')
			sim.DeathTracker.IS_DYING_BUFF = False
			output('6')
			sim._update_facial_overlay()
			output('7')
			sim._remove_multi_motive_buff_trackers()
			output('8')
			sim.reset(ResetReason.RESET_EXPECTED, None, 'Command')
			output('Resurrected sim succesfully 2. If you want to disable all deaths, please, run the command death.toggle and you won´t never die. THANK YOU FOR USING -fer456')
			return True
	output('Sim not found. Do you wrote correctly the name?. Check also you haven´t liberated that spirit in the urnstone.THANK YOU FOR USING -fer456')
	return False